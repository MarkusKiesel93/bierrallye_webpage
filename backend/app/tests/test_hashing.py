from app.hashing import hash_contact


def test_hash_contact():
    email = 'test@test.at'
    salt = 'TEST_SALT'
    assert hash_contact(email, salt) == '095BBE'
