from sqlalchemy.orm import Session,sessionmaker,declarative_base
from sqlalchemy import Column,Integer,String,Date,Boolean,create_engine
from datetime import datetime

engine = create_engine(
    url="sqlite:///./users.db"
)

SessionLocal = sessionmaker(bind=engine)


Base = declarative_base()

class UserDB(Base):
    __tablename__ = "users"
    
    id = Column(Integer,primary_key= True,autoincrement=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    created_at = Column(Date,default=datetime.now())
    fl_active = Column(Boolean,default=True)

    class Config:
        orm_mode = True

Base.metadata.create_all()


