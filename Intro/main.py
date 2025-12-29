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
