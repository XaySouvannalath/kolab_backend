from config.database import database
from models.User import User

async def get_all_users():
    query = "SELECT * FROM `user`"
    result = await database.fetch_all(query=query)
    return result

async def get_user(user_id: int):
    query = "SELECT * FROM `user` WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": user_id})

async def create_user(user: User):
    query = """
    INSERT INTO `user` (username, first_name, last_name, password, is_active, created_by)
    VALUES (:username, :first_name, :last_name, :password, :is_active, :created_by)
    """
    values = {
        "username": user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "password": user.password,
        "is_active": user.is_active,
        "created_by": user.created_by,
    }
    await database.execute(query=query, values=values)

async def update_user(user_id: int, user: User):
    query = """
    UPDATE `user`
    SET username = :username, first_name = :first_name, last_name = :last_name,
        password = :password, is_active = :is_active, created_by = :created_by, 
        last_modified_date = :last_modified_date
    WHERE id = :id
    """
    values = {**user.dict(), "id": user_id}
    await database.execute(query=query, values=values)

async def delete_user(user_id: int):
    query = "DELETE FROM `user` WHERE id = :id"
    await database.execute(query=query, values={"id": user_id})
