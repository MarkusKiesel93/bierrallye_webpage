from fastapi_mail import FastMail, MessageSchema
from twilio.rest import Client

from app.schemas import Team
from app.config import settings
from app.hashing import hash_email


def get_fm() -> FastMail:
    fast_mail = FastMail(settings.mail_config)
    yield fast_mail


def get_twilio_client() -> Client:
    # todo: change to real token
    client = Client(settings.TWILIO_SID, settings.TWILIO_TOKEN)
    yield client


async def send_email(fm: FastMail, email: str, subject: str, body: str):
    message = MessageSchema(
        subject=subject,
        recipients=[email],
        body=body,
        subtype="html"
    )
    await fm.send_message(message)


async def send_sms(client: Client, sms_to: str, body: str):
    # todo: rate_limits
    message = client.messages.create(
        to=sms_to,
        from_=settings.TWILIO_SMS_FROM,
        body=body)
    return message


async def verification_email(fm: FastMail, to: str):
    hash = hash_email(to)
    subject = 'Verifizierung: Bierrallye Irnfritz 2021'
    body = (
        f'<h3> Dein Sicherheitscode für die Bierrallye Irnfritz 2021: </h3>'
        '<p></p>'
        f'<h3> {hash} </h3>'
    )
    await send_email(fm, to, subject, body)


async def verification_sms(client: Client, to: str):
    hash = hash_email(to)
    body = f'Dein Sicherheitscode für die Bierrallye Irnfritz 2021:\n\n{hash}'
    await send_sms(client, to, body)


async def registration_mail(fm: FastMail, team: Team):
    hash = hash_email(team.contact)
    deregistration_link = f'https://{settings.frontend_domain}/deregister/{team.channel}/{team.contact}/{hash}'
    subject = 'Anmeldung: Bierrallye Irnfritz 2021'
    body = (
        f'<h3> Hallo {team.first_name_player_1} und {team.first_name_player_2}, </h3>'
        '<p></p>'
        '<p> Ihr habt euch erfolgreich für die Bierrallye Irnfritz 2021 angemeldet. </p>'
        '<p> Hier nochmals ein Kurzer Überblick der Eckdaten: </p>'
        '<p> Wann: 01.07.2021</p>'
        '<p> Wo: Sportplatz Irnfritz</p>'
        '<p> Stargeld: 50€ per Team </p>'
        '<p> Falls ihr doch keine Zeit habt dann bitte vor der Veranstaltung '
        f'<a href="{deregistration_link}" target="_blank">Abmelden</a></p>'
        f'<p> Link: {deregistration_link} </p>'
        f'<p> Stornonummer: {hash} </p>'
    )
    await send_email(fm, team.contact, subject, body)


def registration_sms(client: Client, team: Team):
    hash = hash_email(team.contact)
    deregistration_link = f'https://{settings.frontend_domain}/deregister/{team.channel}/{team.contact}/{hash}'
    body = (
        f'Hallo {team.first_name_player_1} und {team.first_name_player_2},\n\n'
        'Ihr habt euch erfolgreich für die Bierrallye Irnfritz 2021 angemeldet.\n'
        'Hier nochmals ein Kurzer Überblick der Eckdaten:'
        'Wann: 01.07.2021\n'
        'Wo: Sportplatz Irnfritz\n'
        'Stargeld: 50€ per Team\n'
        'Falls ihr doch keine Zeit habt dann bitte vor der Veranstaltung Abmelden:'
        f'Link: {deregistration_link}\n'
        f'Stornonummer: {team.hash}'
    )
    send_sms(client, team.phone_number, body)