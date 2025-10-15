from sqlalchemy.orm import Session,sessionmaker,declarative_base
from sqlalchemy import Column,Integer,String,Date,Boolean,create_engine
from datetime import datetime,timezone
from passlib.context import CryptContext



engine = create_engine(
    url="sqlite:///./users.db"
)

SessionLocal = sessionmaker(bind=engine)

def get_session():
    try:
        db = SessionLocal()
        yield db 
    finally:
        db.close()


Base = declarative_base()

class UserDB(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key= True,autoincrement=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    created_at = Column(Date,default=datetime.now(timezone.utc))
    fl_active = Column(Boolean,default=True)

    class Config:
        orm_mode = True



