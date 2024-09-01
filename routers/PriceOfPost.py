from typing import List, Union
from fastapi import APIRouter, HTTPException
from models.PriceOfPost import PriceOfPost, PriceOfPostOfInfluencer
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


@router.get("/by_influencer", tags=["price_of_posts"])
async def get(influencer_id: Union[str, None] = None):
    if influencer_id is not None:
        result = await get_price_of_post_by_influencer_id(int(influencer_id))
        if result is None:
            raise HTTPException(status_code=404, detail="Price of post not found")
    else:
        result = await get_price_of_post_by_influencer_id(int(influencer_id))
        if not result:
            raise HTTPException(status_code=404, detail="No prices of posts found")
    return result


@router.post("/save_price_list", tags=["price_of_posts"])
async def save_price_list(influencer_id: int, price_list: List[PriceOfPostOfInfluencer]):
    if influencer_id is not None:
        for pl in price_list:
            print(pl.meta_id)
            if pl.meta_id == 0:
                # insert
                print("saving")
                await create_price(
                    influencer_id=influencer_id,
                    type_of_post_id= pl.id,
                    price= pl.price
                )
                
            else:
                #update
                print("updating")
                await update_price(
                    price_id=pl.meta_id,
                    price=pl.price,
                    influencer_id=influencer_id,
                    type_of_post_id=pl.id,
                )
                
    return price_list
                