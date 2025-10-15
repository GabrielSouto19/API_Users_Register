from pydantic import BaseModel,EmailStr
from datetime import datetime

class UserIn(BaseModel):
    username:str
    email:EmailStr
    password:str

class UserOut(BaseModel):
    id:int 
    username:str
    email:str   
    created_at:datetime
    fl_active: bool