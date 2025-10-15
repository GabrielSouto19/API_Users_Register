from fastapi import FastAPI,Response,HTTPException,Depends
from schemas import UserIn,UserOut
from db import Base,Session,UserDB,get_session,engine
app = FastAPI()

@app.post("/users",status_code=201)
async def add_new_user(user:UserIn,db:Session=Depends(get_session)):
    user_db = UserDB(**user.model_dump())
    db.add(user_db)
    db.commit()
    return Response(content="New recource created",status_code=201)


@app.get("/users",status_code=200,response_model=list[UserOut])
async def get_all_users(search:str | None = None,db:Session=Depends(get_session)):
     
    if search is not None:
        query = db.query(UserDB).filter(UserDB.username.ilike(f"%{search}%")).all()
        return query
    
    query = db.query(UserDB).all()
    if query:    
        return query

    return Response(status_code=204,content="No content")

@app.get("/users/{id}",response_model=UserOut)
async def get_user_by_id(id:int,db:Session=Depends(get_session)):
    user = db.query(UserDB).filter_by(id = id)
    if not user:
        raise HTTPException(status_code=404,detail="Not found!")
    return user


    
@app.on_event("startup")
def start_application():
    Base.metadata.create_all(bind=engine)