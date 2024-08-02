from typing import Union
from fastapi import APIRouter, HTTPException
from models.ImageResource import ImageResource
from cruds.ImageResource import *

router = APIRouter(
    prefix="/image_resources"
)

@router.get("/", tags=["image_resources"])
async def get(id: Union[str, None] = None):
    result = {}
    if id is not None:
        result = await get_image_resource(id)
        if result is None:
            raise HTTPException(status_code=404, detail="ImageResource not found")
    else:
        result = await get_all_image_resources()
        if result is None:
            raise HTTPException(status_code=404, detail="ImageResources not found")
    return result

@router.post("/", tags=["image_resources"])
async def create(image_resource: ImageResource):
    await create_image_resource(image_resource)
    return image_resource

@router.put("/{image_resource_id}", response_model=ImageResource, tags=["image_resources"])
async def update(image_resource_id: int, image_resource: ImageResource):
    existing_image_resource = await get_image_resource(image_resource_id)
    if existing_image_resource is None:
        raise HTTPException(status_code=404, detail="ImageResource not found")
    await update_image_resource(image_resource_id, image_resource)
    return image_resource

@router.delete("/{image_resource_id}", response_model=ImageResource, tags=["image_resources"])
async def delete(image_resource_id: int):
    existing_image_resource = await get_image_resource(image_resource_id)
    if existing_image_resource is None:
        raise HTTPException(status_code=404, detail="ImageResource not found")
    await delete_image_resource(image_resource_id)
    return existing_image_resource
