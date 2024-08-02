from typing import Union
from fastapi import APIRouter, HTTPException
from models.PriceOfPost import PriceOfPost
from cruds.PriceOfPost import *

router = APIRouter(
    prefix="/price_of_posts"
)

@router.get("/", tags=["price_of_posts"])
async def get(id: Union[str, None] = None):
    if id is not None:
        result = await get_price(int(id))
        if result is None:
            raise HTTPException(status_code=404, detail="Price of post not found")
    else:
        result = await get_all_prices()
        if not result:
            raise HTTPException(status_code=404, detail="No prices of posts found")
    return result

@router.post("/", tags=["price_of_posts"])
async def create(price: PriceOfPost):
    await create_price(price)
    return price

@router.put("/{price_id}", response_model=PriceOfPost, tags=["price_of_posts"])
async def update(price_id: int, price: PriceOfPost):
    existing_price = await get_price(price_id)
    if existing_price is None:
        raise HTTPException(status_code=404, detail="Price of post not found")
    await update_price(price_id, price)
    return price

@router.delete("/{price_id}", response_model=PriceOfPost, tags=["price_of_posts"])
async def delete(price_id: int):
    existing_price = await get_price(price_id)
    if existing_price is None:
        raise HTTPException(status_code=404, detail="Price of post not found")
    await delete_price(price_id)
    return existing_price
