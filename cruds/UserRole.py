from typing import List
from config.database import database
from models.UserRole import UserRole

async def get_all_user_roles():
    query = "SELECT * FROM `user_role`"
    result = await database.fetch_all(query=query)
    return result

async def get_user_role(user_role_id: int):
    query = "SELECT * FROM `user_role` WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": user_role_id})

async def get_user_roles_by_user_id(user_id: int) -> List[UserRole]:
    query = """
    SELECT * FROM `user_role` WHERE user_id = :user_id
    """
    result = await database.fetch_all(query=query, values={"user_id": user_id})
    return [UserRole(**row) for row in result]

async def create_user_role(user_role: UserRole):
    query = """
    INSERT INTO `user_role` (role, description, created_by)
    VALUES (:role, :description, :created_by)
    """
    values = {
        "role": user_role.role,
        "description": user_role.description,
        "created_by": user_role.created_by,
    }
    await database.execute(query=query, values=values)

async def update_user_role(user_role_id: int, user_role: UserRole):
    query = """
    UPDATE `user_role`
    SET role = :role, description = :description
    WHERE id = :id
    """
    values = {
        "role": user_role.role,
        "description": user_role.description, 
        "id": user_role_id
        }
    await database.execute(query=query, values=values)

async def delete_user_role(user_role_id: int):
    query = "DELETE FROM `user_role` WHERE id = :id"
    await database.execute(query=query, values={"id": user_role_id})
