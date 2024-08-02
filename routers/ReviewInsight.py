from typing import Union
from fastapi import APIRouter, HTTPException
from models.ReviewInsight import ReviewInsight
from cruds.ReviewInsight import *

router = APIRouter(
    prefix="/review_insights"
)

@router.get("/", tags=["review_insights"])
async def get(id: Union[str, None] = None):
    if id is not None:
        result = await get_review_insight(int(id))
        if result is None:
            raise HTTPException(status_code=404, detail="Review insight not found")
    else:
        result = await get_all_review_insights()
        if not result:
            raise HTTPException(status_code=404, detail="No review insights found")
    return result

@router.post("/", tags=["review_insights"])
async def create(review_insight: ReviewInsight):
    await create_review_insight(review_insight)
    return review_insight

@router.put("/{review_insight_id}", response_model=ReviewInsight, tags=["review_insights"])
async def update(review_insight_id: int, review_insight: ReviewInsight):
    existing_review_insight = await get_review_insight(review_insight_id)
    if existing_review_insight is None:
        raise HTTPException(status_code=404, detail="Review insight not found")
    await update_review_insight(review_insight_id, review_insight)
    return review_insight

@router.delete("/{review_insight_id}", response_model=ReviewInsight, tags=["review_insights"])
async def delete(review_insight_id: int):
    existing_review_insight = await get_review_insight(review_insight_id)
    if existing_review_insight is None:
        raise HTTPException(status_code=404, detail="Review insight not found")
    await delete_review_insight(review_insight_id)
    return existing_review_insight
