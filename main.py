from fastapi import FastAPI

app = FastAPI()

@app.get("/users")
async def add_new_user():
    pass