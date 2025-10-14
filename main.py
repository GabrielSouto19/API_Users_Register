from fastapi import FastAPI,Response,HTTPException
from schemas import UserIn,UserOut

users = []


app = FastAPI()

@app.post("/users",status_code=201)
async def add_new_user(user:UserIn):
    users.append(user)
    return Response(content="New recource created",status_code=201)


@app.get("/users",status_code=200)
async def get_all_users():
    if len(users) >0:
        # return HTTPException(status_code=204)
        return Response(status_code=204,content="No content")
    return users
    