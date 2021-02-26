from app.mail import send_email, registration_mail, deregistration_mail
import pytest


@pytest.mark.asyncio
async def test_send_email(fm):
    email = 'test@test.com'
    subject = 'test subject'
    body = '<p>test body</p>'
    with fm.record_messages() as outbox:
        await send_email(email, subject, body, fm)
        assert len(outbox) == 1

# todo: test registration mail
#   what to exactly test there ?

# todo: test deregistration mail
#   what to exactly test there ?