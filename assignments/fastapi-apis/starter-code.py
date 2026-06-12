from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class Item(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: float

items = {
    1: Item(id=1, name='Sample Item', description='A starter item for the API', price=9.99),
}

@app.get('/')
def read_root():
    return {'message': 'Welcome to the FastAPI assignment!'}

@app.get('/items/{item_id}', response_model=Item)
def read_item(item_id: int):
    if item_id not in items:
        raise HTTPException(status_code=404, detail='Item not found')
    return items[item_id]

@app.post('/items/', response_model=Item)
def create_item(item: Item):
    if item.id in items:
        raise HTTPException(status_code=400, detail='Item already exists')
    items[item.id] = item
    return item

# Run this app with:
# uvicorn assignments.fastapi-apis.starter-code:app --reload
