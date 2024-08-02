from typing import Union
from fastapi import APIRouter, HTTPException
from models.ContentStyle import ContentStyle
from cruds.ContentStyle import *

router = APIRouter(
    prefix="/content_style"
)

@router.get("/", tags=["content_style"])
async def get(id: Union[str, None] = None):
    result = {}
    if id is not None:
        result = await get_content_style(id)
        if result is None:
            raise HTTPException(status_code=404, detail="ContentStyle not found")
    else:
        result = await get_all_content_styles()
        if result is None:
            raise HTTPException(status_code=404, detail="ContentStyles not found")
    return result

@router.post("/", tags=["content_style"])
async def create(content_style: ContentStyle):
    await create_content_style(content_style)
    return content_style

@router.put("/{content_style_id}", response_model=ContentStyle, tags=["content_style"])
async def update(content_style_id: int, content_style: ContentStyle):
    existing_content_style = await get_content_style(content_style_id)
    if existing_content_style is None:
        raise HTTPException(status_code=404, detail="ContentStyle not found")
    await update_content_style(content_style_id, content_style)
    return content_style

@router.delete("/{content_style_id}", response_model=ContentStyle, tags=["content_style"])
async def delete(content_style_id: int):
    existing_content_style = await get_content_style(content_style_id)
    if existing_content_style is None:
        raise HTTPException(status_code=404, detail="ContentStyle not found")
    await delete_content_style(content_style_id)
    return existing_content_style
