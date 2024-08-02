from typing import Union
from fastapi import APIRouter, HTTPException
from models.Menu import Menu
from cruds.Menu import *

router = APIRouter(
    prefix="/menus"
)

@router.get("/", tags=["menus"])
async def get(id: Union[str, None] = None):
    if id is not None:
        result = await get_menu(int(id))
        if result is None:
            raise HTTPException(status_code=404, detail="Menu not found")
    else:
        result = await get_all_menus()
        if not result:
            raise HTTPException(status_code=404, detail="No menus found")
    return result

@router.post("/", tags=["menus"])
async def create(menu: Menu):
    await create_menu(menu)
    return menu

@router.put("/{menu_id}", response_model=Menu, tags=["menus"])
async def update(menu_id: int, menu: Menu):
    existing_menu = await get_menu(menu_id)
    if existing_menu is None:
        raise HTTPException(status_code=404, detail="Menu not found")
    await update_menu(menu_id, menu)
    return menu

@router.delete("/{menu_id}", response_model=Menu, tags=["menus"])
async def delete(menu_id: int):
    existing_menu = await get_menu(menu_id)
    if existing_menu is None:
        raise HTTPException(status_code=404, detail="Menu not found")
    await delete_menu(menu_id)
    return existing_menu
