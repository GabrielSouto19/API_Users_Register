from passlib.hash import bcrypt
from passlib.hash import bcrypt

h = bcrypt.hash("password")
h = bcrypt.hash("password")

print(h)



def hash_password(password:str):
    hashed_password = bcrypt.hash(password)
    return hashed_password

def verifify_password(pwd,hashed_pwd):
    return bcrypt.verify(pwd,hashed_pwd)
