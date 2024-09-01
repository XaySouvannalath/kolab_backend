from config.database import database
from models.Menu import Menu

async def get_all_menus():
    query = "SELECT * FROM menu"
    result = await database.fetch_all(query=query)
    return result

async def get_menu(menu_id: int):
    query = "SELECT * FROM menu WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": menu_id})

async def create_menu(menu: Menu):
    query = """
    INSERT INTO menu (menu, route, description, created_by)
    VALUES (:menu, :route, :description, :created_by)
    """
    values = {
        "menu": menu.menu,
        "route": menu.route,
        "description": menu.description,
        "created_by": menu.created_by,
    }
    await database.execute(query=query, values=values)

async def update_menu(menu_id: int, menu: Menu):
    query = """
    UPDATE menu
    SET menu = :menu, route = :route, description = :description
    WHERE id = :id
    """
    values = {
        "menu": menu.menu,
        "route": menu.route,
        "description": menu.description,
        "id": menu_id}
    await database.execute(query=query, values=values)

async def delete_menu(menu_id: int):
    query = "DELETE FROM menu WHERE id = :id"
    await database.execute(query=query, values={"id": menu_id})
