from typing import Union
from fastapi import APIRouter, HTTPException
from models.User import User
from cruds.User import *

router = APIRouter(
    prefix="/users"
)

@router.get("/", tags=["users"])
async def get(id: Union[int, None] = None):
    if id is not None:
        result = await get_user(id)
        if result is None:
            raise HTTPException(status_code=404, detail="User not found")
    else:
        result = await get_all_users()
        if not result:
            raise HTTPException(status_code=404, detail="No users found")
    return result

@router.post("/", tags=["users"])
async def create(user: User):
    await create_user(user)
    return user

@router.put("/{user_id}", response_model=User, tags=["users"])
async def update(user_id: int, user: User):
    existing_user = await get_user(user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    await update_user(user_id, user)
    return user

@router.delete("/{user_id}", response_model=User, tags=["users"])
async def delete(user_id: int):
    existing_user = await get_user(user_id)
    if existing_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    await delete_user(user_id)
    return existing_user
