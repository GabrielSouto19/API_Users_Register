from passlib.hash import bcrypt
import jwt
from datetime import datetime,timedelta,timezone
from db import UserDB,get_session
from fastapi import Depends,HTTPException,status
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials


# extractor HTTP Bearer
bearer_scheme = HTTPBearer()


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
        # use string for 'sub' to follow common JWT practices
        "sub": str(user_id),
        # exp and iat as integer timestamps
        "exp": int(expire.timestamp()),
        "iat": int(datetime.now(timezone.utc).timestamp())
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)
    return token 

def verify_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme), db: Session = Depends(get_session)):
    """Dependência que recebe credenciais HTTP Bearer, decodifica o JWT e retorna o usuário.

    Use em rotas como: current_user = Depends(verify_token)
    """
    token = credentials.credentials
    print(token)
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token expirado")
    except jwt.InvalidTokenError as e:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"Token inválido:{str(e)}")

    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token sem sub")

    # try convert to int for numeric PKs, fallback to string lookup
    try:
        user_pk = int(user_id)
    except Exception:
        user_pk = None

    if user_pk is not None:
        user = db.query(UserDB).filter(UserDB.id == user_pk).first()
    else:
        user = db.query(UserDB).filter(UserDB.id == user_id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Usuário não encontrado")
    return user
    

# get_current_user is no longer required; use verify_token as dependency
if __name__ == "__main__":
    print(create_acess_token(1))