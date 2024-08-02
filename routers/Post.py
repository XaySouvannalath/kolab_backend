from typing import Union
from fastapi import APIRouter, HTTPException
from models.Post import Post
from cruds.Post import *

router = APIRouter(
    prefix="/posts"
)

@router.get("/", tags=["posts"])
async def get(id: Union[str, None] = None):
    if id is not None:
        result = await get_post(int(id))
        if result is None:
            raise HTTPException(status_code=404, detail="Post not found")
    else:
        result = await get_all_posts()
        if not result:
            raise HTTPException(status_code=404, detail="No posts found")
    return result

@router.post("/", tags=["posts"])
async def create(post: Post):
    await create_post(post)
    return post

@router.put("/{post_id}", response_model=Post, tags=["posts"])
async def update(post_id: int, post: Post):
    existing_post = await get_post(post_id)
    if existing_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    await update_post(post_id, post)
    return post

@router.delete("/{post_id}", response_model=Post, tags=["posts"])
async def delete(post_id: int):
    existing_post = await get_post(post_id)
    if existing_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    await delete_post(post_id)
    return existing_post
