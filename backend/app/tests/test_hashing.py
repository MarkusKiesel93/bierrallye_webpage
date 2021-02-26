from app.hashing import hash_email


def test_hash_email():
    email = 'test@test.at'
    salt = 'TEST_SALT'
    assert hash_email(email, salt) == '095BBE'
