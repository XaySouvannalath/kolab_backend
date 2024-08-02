from typing import Union
from fastapi import APIRouter, HTTPException
from models.InfluencerReview import InfluencerReview
from cruds.InfluencerReview import *

router = APIRouter(
    prefix="/influencer_reviews"
)

@router.get("/", tags=["influencer_reviews"])
async def get(id: Union[str, None] = None):
    if id is not None:
        result = await get_influencer_review(int(id))
        if result is None:
            raise HTTPException(status_code=404, detail="InfluencerReview not found")
    else:
        result = await get_all_influencer_reviews()
        if not result:
            raise HTTPException(status_code=404, detail="No InfluencerReviews found")
    return result

@router.post("/", tags=["influencer_reviews"])
async def create(influencer_review: InfluencerReview):
    await create_influencer_review(influencer_review)
    return influencer_review

@router.put("/{review_id}", response_model=InfluencerReview, tags=["influencer_reviews"])
async def update(review_id: int, influencer_review: InfluencerReview):
    existing_review = await get_influencer_review(review_id)
    if existing_review is None:
        raise HTTPException(status_code=404, detail="InfluencerReview not found")
    await update_influencer_review(review_id, influencer_review)
    return influencer_review

@router.delete("/{review_id}", response_model=InfluencerReview, tags=["influencer_reviews"])
async def delete(review_id: int):
    existing_review = await get_influencer_review(review_id)
    if existing_review is None:
        raise HTTPException(status_code=404, detail="InfluencerReview not found")
    await delete_influencer_review(review_id)
    return existing_review
