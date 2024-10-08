from config.database import database
from models.ContentStyle import ContentStyle

async def get_all_content_styles():
    query = "SELECT * FROM content_style"
    result = await database.fetch_all(query=query)
    return result

async def get_content_style(content_style_id: int):
    query = "SELECT * FROM content_style WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": content_style_id})

async def create_content_style(content_style: ContentStyle):
    query = """
    INSERT INTO content_style (name, description)
    VALUES (:name, :description)
    """
    values = {
        "name": content_style.name,
        "description": content_style.description
    }
    await database.execute(query=query, values=values)

async def update_content_style(content_style_id: int, content_style: ContentStyle):
    query = """
    UPDATE content_style
    SET name = :name, description = :description
    WHERE id = :id
    """
    values = {
        "name": content_style.name,
        "description": content_style.description
        , "id": content_style_id}
    await database.execute(query=query, values=values)

async def delete_content_style(content_style_id: int):
    query = "DELETE FROM content_style WHERE id = :id"
    await database.execute(query=query, values={"id": content_style_id})
