from config.database import database
from models.Post import Post

async def get_all_posts():
    query = "SELECT * FROM posts"
    result = await database.fetch_all(query=query)
    return result

async def get_post(post_id: int):
    query = "SELECT * FROM posts WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": post_id})

async def create_post(post: Post):
    query = """
    INSERT INTO posts (name, description, created_by)
    VALUES (:name, :description, :created_by)
    """
    values = {
        "name": post.name,
        "description": post.description,
        "created_by": post.created_by,
    }
    await database.execute(query=query, values=values)

async def update_post(post_id: int, post: Post):
    query = """
    UPDATE posts
    SET name = :name, description = :description
    WHERE id = :id
    """
    values = {
        "name": post.name,
        "description": post.description,
        "id": post_id
        }
    await database.execute(query=query, values=values)

async def delete_post(post_id: int):
    query = "DELETE FROM posts WHERE id = :id"
    await database.execute(query=query, values={"id": post_id})
