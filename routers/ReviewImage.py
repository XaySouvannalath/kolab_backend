from typing import Union
from fastapi import APIRouter, HTTPException
from models.ReviewImage import ReviewImage
from cruds.ReviewImage import *

router = APIRouter(
    prefix="/review_images"
)

@router.get("/", tags=["review_images"])
async def get(id: Union[str, None] = None):
    if id is not None:
        result = await get_review_image(int(id))
        if result is None:
            raise HTTPException(status_code=404, detail="Review image not found")
    else:
        result = await get_all_review_images()
        if not result:
            raise HTTPException(status_code=404, detail="No review images found")
    return result

@router.post("/", tags=["review_images"])
async def create(review_image: ReviewImage):
    await create_review_image(review_image)
    return review_image

@router.put("/{review_image_id}", response_model=ReviewImage, tags=["review_images"])
async def update(review_image_id: int, review_image: ReviewImage):
    existing_review_image = await get_review_image(review_image_id)
    if existing_review_image is None:
        raise HTTPException(status_code=404, detail="Review image not found")
    await update_review_image(review_image_id, review_image)
    return review_image

@router.delete("/{review_image_id}", response_model=ReviewImage, tags=["review_images"])
async def delete(review_image_id: int):
    existing_review_image = await get_review_image(review_image_id)
    if existing_review_image is None:
        raise HTTPException(status_code=404, detail="Review image not found")
    await delete_review_image(review_image_id)
    return existing_review_image
