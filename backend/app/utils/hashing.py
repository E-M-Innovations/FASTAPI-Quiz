from passlib.hash import bcrypt


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#
#           HASHING
#
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


def hash_password(password: str):
    return bcrypt.hash(password)


def verify_hash(password, hash):
    return bcrypt.verify(password, hash)
