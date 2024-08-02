from config.database import database
from models.RoleMenu import RoleMenu

async def get_all_role_menus():
    query = "SELECT * FROM role_menu"
    result = await database.fetch_all(query=query)
    return result

async def get_role_menu(role_menu_id: int):
    query = "SELECT * FROM role_menu WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": role_menu_id})

async def create_role_menu(role_menu: RoleMenu):
    query = """
    INSERT INTO role_menu (role_id, menu_id, created_by)
    VALUES (:role_id, :menu_id, :created_by)
    """
    values = {
        "role_id": role_menu.role_id,
        "menu_id": role_menu.menu_id,
        "created_by": role_menu.created_by,
    }
    await database.execute(query=query, values=values)

async def update_role_menu(role_menu_id: int, role_menu: RoleMenu):
    query = """
    UPDATE role_menu
    SET role_id = :role_id, menu_id = :menu_id, 
        created_by = :created_by, last_modified_date = :last_modified_date
    WHERE id = :id
    """
    values = {**role_menu.dict(), "id": role_menu_id}
    await database.execute(query=query, values=values)

async def delete_role_menu(role_menu_id: int):
    query = "DELETE FROM role_menu WHERE id = :id"
    await database.execute(query=query, values={"id": role_menu_id})
