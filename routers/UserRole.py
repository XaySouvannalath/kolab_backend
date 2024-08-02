from typing import Union, List
from fastapi import APIRouter, HTTPException
from models.UserRole import UserRole
from cruds.UserRole import *

router = APIRouter(
    prefix="/user_roles"
)

@router.get("/", tags=["user_roles"])
async def get(id: Union[int, None] = None):
    if id is not None:
        result = await get_user_role(id)
        if result is None:
            raise HTTPException(status_code=404, detail="User role not found")
    else:
        result = await get_all_user_roles()
        if not result:
            raise HTTPException(status_code=404, detail="No user roles found")
    return result

@router.post("/", tags=["user_roles"])
async def create(user_role: UserRole):
    await create_user_role(user_role)
    return user_role

@router.put("/{user_role_id}", response_model=UserRole, tags=["user_roles"])
async def update(user_role_id: int, user_role: UserRole):
    existing_user_role = await get_user_role(user_role_id)
    if existing_user_role is None:
        raise HTTPException(status_code=404, detail="User role not found")
    await update_user_role(user_role_id, user_role)
    return user_role

@router.delete("/{user_role_id}", response_model=UserRole, tags=["user_roles"])
async def delete(user_role_id: int):
    existing_user_role = await get_user_role(user_role_id)
    if existing_user_role is None:
        raise HTTPException(status_code=404, detail="User role not found")
    await delete_user_role(user_role_id)
    return existing_user_role

# @router.get("/user/{user_id}", response_model=List[UserRole], tags=["user_roles"])
# async def get_user_roles_by_user_id(user_id: int):
#     user_roles = await get_user_roles_by_user_id(user_id)
#     if not user_roles:
#         raise HTTPException(status_code=404, detail="User roles not found for this user")
#     return user_roles