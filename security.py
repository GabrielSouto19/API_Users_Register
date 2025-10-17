from passlib.hash import bcrypt
import jwt
from datetime import datetime,timedelta,timezone
from db import UserDB,get_session
from fastapi import Depends,HTTPException
from sqlalchemy.orm import Session 


ACCESS_TOKEN_EXPIRE_MINUTES = 30
ALGORITHM = "HS256"
SECRET_KEY = "meu_segredo_muito_bom"

def hash_password(password:str):
    hashed_password = bcrypt.hash(password)
    return hashed_password

def verifify_password(pwd,hashed_pwd):
    return bcrypt.verify(pwd,hashed_pwd)


def create_acess_token(user_id:int,expire_minutes:int=ACCESS_TOKEN_EXPIRE_MINUTES)-> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=expire_minutes)
    payload = {
        "sub":user_id,
        "exp":expire.timestamp(),
        "iat": datetime.now(timezone.utc).timestamp()
    }
    token = jwt.encode(payload,SECRET_KEY,ALGORITHM)
    return token 

# def verify_token(token:str):
#     try:
#         payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])
    

if __name__ == "__main__":
    print(create_acess_token(1))