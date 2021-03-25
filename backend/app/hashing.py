from hashlib import sha256

from app.config import settings

SALT = settings.secret_key

# todo rename to hash contact
def hash_email(email, salt=SALT):
    return sha256(salt.encode() + email.encode()).hexdigest().upper()[:6]
