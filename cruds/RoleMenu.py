from config.database import database
from models.RoleMenu import RoleMenu

async def get_all_role_menus():
    query = "SELECT * FROM role_menu"
    result = await database.fetch_all(query=query)
    return result

async def get_role_menu(role_menu_id: int):
    query = "SELECT * FROM role_menu WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": role_menu_id})


async def get_role_menu_by_role_id(role_id: int):
    """
    Retrieves the role menu details associated with a specific role ID.

    Finds and returns a list of role menu entries that match the given role ID
    by joining the role_menu and menu tables in the database. The resulting data
    includes details about the menu and its corresponding route.

    Parameters:
    role_id: int
        The ID of the role for which the menu information will be retrieved.

    Returns:
    list[dict]
        A list of dictionaries, where each dictionary represents a role menu
        entry containing details such as the menu ID, role ID, menu, and route.

    Raises:
    ValueError
        If the database query fails or returns invalid data.
    """
    query = """
    select
    a.*,
    b.menu,
    b.route
    from role_menu a inner join menu b
    on a.menu_id = b.id
    and a.role_id = :role_id
    ;
    """
    return await database.fetch_all(query=query, values={"role_id": role_id})


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
