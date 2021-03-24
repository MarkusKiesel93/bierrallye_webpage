from app.mail import send_email
import pytest


@pytest.mark.asyncio
async def test_send_email(fm):
    email = 'test@test.com'
    subject = 'test subject'
    body = '<p>test body</p>'
    with fm.record_messages() as outbox:
        await send_email(fm, email, subject, body)
        assert len(outbox) == 1
