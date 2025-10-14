from pydantic import BaseModel,EmailStr

class UserIn(BaseModel):
    username:str
    email:EmailStr
    password:str

class UserOut(BaseModel):
    # id:int | None
    username:str
    email:str   
