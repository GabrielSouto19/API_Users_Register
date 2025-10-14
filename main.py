from fastapi import FastAPI,Response,HTTPException
from schemas import UserIn,UserOut

users:list = []


app = FastAPI()

@app.post("/users",status_code=201)
async def add_new_user(user:UserIn):
    users.append(user)
    return Response(content="New recource created",status_code=201)


@app.get("/users",status_code=200,response_model=list[UserOut])
async def get_all_users(query:str | None = None):
    
    if query is not None:
        results = []

        for i in users:
            if query in i.get("nome") or query in i.get("email"):
                results.append(i)
            
        return results

    if len(users) >0:
        # return HTTPException(status_code=204)
        return users
    return Response(status_code=204,content="No content")

    