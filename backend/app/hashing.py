from hashlib import sha256

from app.config import settings

SALT = settings.secret_key


def hash_email(email, salt=SALT):
    return sha256(salt.encode() + email.encode()).hexdigest().upper()[:6]
