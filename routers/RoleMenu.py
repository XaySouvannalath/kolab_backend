from typing import Union
from fastapi import APIRouter, HTTPException
from models.RoleMenu import RoleMenu
from cruds.RoleMenu import *

router = APIRouter(
    prefix="/role_menus"
)

@router.get("/", tags=["role_menus"])
async def get(id: Union[str, None] = None):
    if id is not None:
        result = await get_role_menu(int(id))
        if result is None:
            raise HTTPException(status_code=404, detail="Role menu not found")
    else:
        result = await get_all_role_menus()
        if not result:
            raise HTTPException(status_code=404, detail="No role menus found")
    return result

@router.post("/", tags=["role_menus"])
async def create(role_menu: RoleMenu):
    await create_role_menu(role_menu)
    return role_menu

@router.put("/{role_menu_id}", response_model=RoleMenu, tags=["role_menus"])
async def update(role_menu_id: int, role_menu: RoleMenu):
    existing_role_menu = await get_role_menu(role_menu_id)
    if existing_role_menu is None:
        raise HTTPException(status_code=404, detail="Role menu not found")
    await update_role_menu(role_menu_id, role_menu)
    return role_menu

@router.delete("/{role_menu_id}", response_model=RoleMenu, tags=["role_menus"])
async def delete(role_menu_id: int):
    existing_role_menu = await get_role_menu(role_menu_id)
    if existing_role_menu is None:
        raise HTTPException(status_code=404, detail="Role menu not found")
    await delete_role_menu(role_menu_id)
    return existing_role_menu
