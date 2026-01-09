from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()
@app.get("/")
async def root():
    return {"message":"Hello world"}

class Item(BaseModel):
    name:str
    describation:str|None=None
    price:float
    tax:float|None=None

@app.post("/items")
async def creat_item(item:Item):
    item_dict=item.dict()
    if item.tax:
        price_with_tax=item.price+(item.price*item.tax)
        item_dict.update({"total_price":price_with_tax})
    return item_dict

@app.put("/items/item_id")
async def update_item(item_id:int,item:Item):
    return {"item_id":item_id,**item.dict()}