from config.database import database
from models.User import User

async def get_all_users():
    query = """
    
        select 
        a.*,
        b.role as user_role
        from user a
        inner join user_role b on b.id = a.user_role_id
    """
    result = await database.fetch_all(query=query)
    return result

async def get_user(user_id: int):
    query = "SELECT * FROM `user` WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": user_id})

async def create_user(user: User):
    query = """
    INSERT INTO `user` (username, first_name, last_name, password, is_active, created_by, user_role_id)
    VALUES (:username, :first_name, :last_name, :password, :is_active, :created_by, :user_role_id)
    """
    values = {
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "password": user.password,
        "is_active": user.is_active,
        "created_by": user.created_by,
        "user_role_id": user.user_role_id
    }
    await database.execute(query=query, values=values)

async def update_user(user_id: int, user: User):
    query = """
        UPDATE `user`
        SET username = :username, first_name = :first_name, last_name = :last_name,
            is_active = :is_active, user_role_id = :user_role_id
        WHERE id = :id
    """
    values = {
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "is_active": user.is_active,
        "user_role_id": user.user_role_id,
        "id": user_id
    }
    await database.execute(query=query, values=values)


async def delete_user(user_id: int):
    query = "DELETE FROM `user` WHERE id = :id"
    await database.execute(query=query, values={"id": user_id})
