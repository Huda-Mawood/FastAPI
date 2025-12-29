from fastapi import FastAPI
from enum import Enum
app=FastAPI()
@app.get("/")
async def root():
    return {"message":"Hello World"}

@app.post("/")
async def post():
    return{"message":"this is a post request"}
@app.put("/",description="this is a put endpoint")
async def put():
    return{"message":"this is a put request"}

@app.get("/users")
async def list_users():
    return {"message":"this is user list"}
@app.get("/users/1",include_in_schema=False)
async def admin_user():
    return {"message":"this is admin user"}
@app.get("/users/{user_id}")
async def get_user(user_id:int):
    return {"message":user_id}
class UserList(str,Enum):
    admin=1
    manager=2
    user=3

@app.get("/{user_type}/{user_id}")
async def get_user_type(user_type:UserList,user_id):
    return{"user":{user_type.name,user_id}}
