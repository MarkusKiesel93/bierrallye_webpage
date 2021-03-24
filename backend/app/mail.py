from fastapi_mail import FastMail, MessageSchema

from app.schemas import Team, TeamCreated
from app.config import settings


def get_fm() -> FastMail:
    fast_mail = FastMail(settings.mail_config)
    yield fast_mail


async def send_email(fm: FastMail, email: str, subject: str, body: str):
    message = MessageSchema(
        subject=subject,
        recipients=[email],
        body=body,
        subtype="html"
    )
    await fm.send_message(message)


async def verification_mail(fm: FastMail, team: TeamCreated):
    verification_link = f'https://{settings.frontend_domain}/verify/{team.email}/{team.hash}'
    subject = 'Verifizierung: Bierrallye Irnfritz 2021'
    body = (
        f'<h3> Hallo {team.first_name_player_1} und {team.first_name_player_2}, </h3>'
        '<p></p>'
        '<p> Schließt hier eure Anmeldung ab: '
        f'<a href="{verification_link}" target="_blank">Wir sind dabei</a></p>'
        f'<p> Link: {verification_link} </p>'
    )
    await send_email(fm, team.email, subject, body)


async def registration_mail(fm: FastMail, team: TeamCreated):
    deregistration_link = f'https://{settings.frontend_domain}/deregister/{team.email}/{team.hash}'
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
        f'<p> Stornocode: {team.hash} </p>'
    )
    await send_email(fm, team.email, subject, body)


async def deregistration_mail(fm: FastMail, team: Team):
    subject = 'Abmeldung: Bierrallye Irnfritz 2021'
    body = (
        f'<h3> Hallo {team.first_name_player_1} und {team.first_name_player_2}, </h3>'
        '<p></p>'
        '<p> Ihr habt euch von der Bierrallye Irnfritz 2021 abgemeldet. </p>'
    )
    await send_email(fm, team.email, subject, body)
