from passlib.hash import bcrypt
from passlib.hash import bcrypt
import jwt
from datetime import datetime,timedelta,timezone

ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = "HS256"
SECRET_KEY = ""

def hash_password(password:str):
    hashed_password = bcrypt.hash(password)
    return hashed_password

def verifify_password(pwd,hashed_pwd):
    return bcrypt.verify(pwd,hashed_pwd)

def create_token(user_id,duration_token=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)):
    expiration_date = datetime.now(timezone.utc) + duration_token
    dic_info ={
        "sub":user_id,
        "expiration_date":str(expiration_date)
    } 

    print(dic_info)
    encoded_jwt = jwt.encode(dic_info,key=SECRET_KEY,algorithm=ALGORITHM)

    return encoded_jwt


    

if __name__ == "__main__":
    print(create_token({"fala comigo":"Marcolas"}))
