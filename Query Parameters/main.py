from fastapi import FastAPI
app=FastAPI()
@app.get("/")
async def root():
    return {"message":"Hello world"}

items = [
    {"id":1 , "name":"book" , "price":"15" , "stock": True},
    {"id":2 , "name":"game" , "price":"50" , "stock": True},
    {"id":3 , "name":"cd" , "price":"30" , "stock": True},
    {"id":4 , "name":"magazine" , "price":"10" , "stock": False},
    {"id":5 , "name":"book" , "price":"10" , "stock": True},
    {"id":6 , "name":"game" , "price":"10" , "stock": True}
]
@app.get("/items")
async def list_items(
        start:int=0,
        end:int=10,
        id:int=None,
        name:str=None
):
    if id:
        item=next((item for item in items if item["id"]==id),None)
        if item:
            return item
        else:
            return {"message":"item not found"}
    if name:
        filter=[]
        for item in items:
            if item["name"]==name:
                filter.append(item)
        return filter
    return items[start:start+end]

@app.get("/items/prices")
async def sort_price(range:int=None):
    sorted_items=sorted(items,key=lambda x:x["price"],reverse=True)
    if range:
        price_range=[item for item in sorted_items if item["price"]<=str(range)]
        return price_range
    else:
        return sorted_items

@app.get("/items/stocks")
async def get_stock(in_stock:bool=True):
    if not in_stock:
        item=[item for item in items if item["stock"]==False]
        return item
    else:
        item=[item for item in items if item["stock"]==True]
        return item
