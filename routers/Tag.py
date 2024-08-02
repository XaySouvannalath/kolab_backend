from typing import Union
from fastapi import APIRouter, HTTPException
from models.Tag import Tag
from cruds.Tag import *

router = APIRouter(
    prefix="/tags"
)

@router.get("/", tags=["tags"])
async def get(id: Union[str, None] = None):
    if id is not None:
        result = await get_tag(int(id))
        if result is None:
            raise HTTPException(status_code=404, detail="Tag not found")
    else:
        result = await get_all_tags()
        if not result:
            raise HTTPException(status_code=404, detail="No tags found")
    return result

@router.post("/", tags=["tags"])
async def create(tag: Tag):
    await create_tag(tag)
    return tag

@router.put("/{tag_id}", response_model=Tag, tags=["tags"])
async def update(tag_id: int, tag: Tag):
    existing_tag = await get_tag(tag_id)
    if existing_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    await update_tag(tag_id, tag)
    return tag

@router.delete("/{tag_id}", response_model=Tag, tags=["tags"])
async def delete(tag_id: int):
    existing_tag = await get_tag(tag_id)
    if existing_tag is None:
        raise HTTPException(status_code=404, detail="Tag not found")
    await delete_tag(tag_id)
    return existing_tag
