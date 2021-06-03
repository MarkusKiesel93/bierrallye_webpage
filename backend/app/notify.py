from fastapi_mail import FastMail, MessageSchema
from twilio.rest import Client

from app.schemas import Team
from app.config import settings, bier_settings
from app.hashing import hash_contact


def get_fm() -> FastMail:
    fast_mail = FastMail(settings.mail_config)
    yield fast_mail


class TwilioClient():
    def __init__(self, sid=settings.twilio_sid, token=settings.twilio_token, sms_from=settings.twilio_sms_from):
        self.base_client = Client(sid, token)
        self.sms_from = sms_from


def get_twilio_client() -> TwilioClient:
    yield TwilioClient()


async def send_email(fm: FastMail, email: str, subject: str, body: str):
    message = MessageSchema(
        subject=subject,
        recipients=[email],
        body=body,
        subtype="html"
    )
    await fm.send_message(message)


async def send_sms(client: TwilioClient, sms_to: str, body: str):
    # todo: rate_limits
    message = client.base_client.messages.create(
        to=sms_to,
        from_=client.sms_from,
        body=body)
    return message


async def verification_email(fm: FastMail, to: str):
    hash = hash_contact(to)
    subject = 'Verifizierung: Bierrallye Irnfritz'
    body = (
        f'<h3> Dein Code lautet: </h3>'
        '<p></p>'
        f'<h3> {hash} </h3>'
    )
    await send_email(fm, to, subject, body)


async def verification_sms(client: TwilioClient, to: str):
    hash = hash_contact(to)
    body = f'Dein Verifizierungscode für die Bierrallye Irnfritz:\n\n{hash}'
    await send_sms(client, to, body)


async def registration_mail(fm: FastMail, team: Team):
    hash = hash_contact(team.contact)
    deregistration_link = f'https://{settings.frontend_domain}/deregister/{team.channel}/{team.contact}/{hash}'
    start_time = bier_settings.get_start_time(team.start_block)
    subject = 'Anmeldung: Bierrallye Irnfritz 2021'
    body = (
        f'<h3> Hallo {team.first_name_player_1} und {team.first_name_player_2}, </h3>'
        '<p></p>'
        '<p> Ihr habt euch erfolgreich für die Bierrallye Irnfritz 2021 angemeldet. </p>'
        '<p> Hier nochmals die Eckdaten: </p>'
        '<ul>'
        f'<li> Anmeldezeit (vor Ort): {start_time}</li>'
        '<li> Wo: Sportplatz Irnfritz</li>'
        '<li> Stargeld: 50€ per Team </li>'
        '</ul>'
        '<p> Falls ihr doch keine Zeit habt dann bitte vor der Veranstaltung '
        f'<a href="{deregistration_link}" target="_blank">Abmelden</a></p>'
        f'<p> Link: {deregistration_link} </p>'
        f'<p> Stornonummer: {hash} </p>'
    )
    await send_email(fm, team.contact, subject, body)


async def registration_sms(client: TwilioClient, team: Team):
    hash = hash_contact(team.contact)
    start_time = bier_settings.get_start_time(team.start_block)
    deregistration_link = f'https://{settings.frontend_domain}/deregister/{team.channel}/{team.contact}/{hash}'
    body = (
        'Ihr habt euch erfolgreich für die Bierrallye Irnfritz angemeldet.\n'
        f'Anmeldezeit (vor Ort): {start_time}\n'
        f'Abmeldung unter: {deregistration_link}\n'
        f'Stornonummer: {hash}'
    )
    await send_sms(client, team.contact, body)


async def send_mass_mail(fm: FastMail, teams: list, type: str):
    for team in teams:
        subject, body = get_message_by_type(
            type,
            team.contact,
            hash_contact(team.contact),
            team.first_name_player_1,
            team.first_name_player_2)
        await send_email(fm, team.contact, subject, body)


def get_message_by_type(type: str, email: str, hash: str, name1: str, name2: str):
    deregistration_link = f'https://{settings.frontend_domain}/deregister/email/{email}/{hash}'
    if type == 'date_change':
        subject = 'VERSCHOBEN Bier Rallye der JVP Irnfritz'
        body = (
        f'<h3> Hallo {name1} und {name2}, </h3>'
        '<p></p>'
        '<p>Wie ihr vielleicht schon auf Facebook oder Instagram gelesen habt, wurde unsere Bier-Rallye auf den 17. Juli 2021 verschoben. Eure Anmeldung, der Startblock und die Startzeit bleiben natürlich aufrecht. </p>'
        
        '<p> WICHTIG: Solltet ihr bereits wissen, dass ihr am 17. Juli keine Zeit habt, seid bitte so fair und meldet euch unter folgendem Link ab, damit wir den Platz an eines der wartenden Teams vergeben können: '
        f'<a href="{deregistration_link}" target="_blank">Abmelden</a><br>'
        f'Link: {deregistration_link} <br>'
        f'Stornonummer: {hash} </p>'
        '<p></p>'
        '<p>Bei Fragen meldet euch gerne bei uns! Wir freuen uns auf euch :) </p>'
        '<p></p>'
        '<p>Prost,<br>'
        'die JVP Irnfritz</p>'
    )
    return subject, body