from typing import List, Union
from fastapi import APIRouter, HTTPException
from models.InfluencerReview import InfluencerReview, InfluencerReviewResponse
from cruds.InfluencerReview import *
from cruds.ReviewImage import *

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
            result = []
    return result
@router.get("/by_influencer_id", tags=["influencer_reviews"]) 
async def get_by_influencer_id(influencer_id: Union[str, None] = None) -> List[InfluencerReviewResponse]:
    if id is not None:
        result = await get_influencer_review_by_influencer_id(int(influencer_id))
        if result is None:
            result = []
            
    review_response = []
    
    for r in result:
        print(r["id"])
        images = await get_review_image(r["id"])
        print(images)

        # Map the tags into a list of InfluencerTagModel
      #  image_model = [ReviewImage(id=image["id"], image_name=image["image_name"]) for image in images]
        image_model = []
        if images is not None:
            for img in images:
                print(img["id"])
                image_model.append(
                    ReviewImage(
                        id=img["id"],
                        filename=img["filename"],
                        review_id=img["review_id"],
                        created_date=img["created_date"]
                    )
                )
        review_response.append(
            InfluencerReviewResponse(
                brand=r["brand"],
                campaign_name=r["campaign_name"],
                start_at=r["start_at"],
                end_at=r["end_at"],
                id=r["id"],
                engagement=r["engagement"],
                impression=r["impression"],
                reach=r["reach"],
                score=r["score"],
                influencer_id=r["influencer_id"],
                images=image_model
            )
        )
    return review_response

@router.post("/", tags=["influencer_reviews"])
async def create(influencer_review: InfluencerReview):
    result = await create_influencer_review(influencer_review)
    return {
        "id": result
    }

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
