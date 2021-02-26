from hashlib import sha256

from app.config import settings


def hash_email(email):
    salt = settings.secret_key
    return sha256(salt.encode() + email.encode()).hexdigest().upper()[:6]
