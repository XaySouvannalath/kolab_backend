from config.database import database
from models.Tag import Tag

async def get_all_tags():
    query = "SELECT * FROM tag"
    result = await database.fetch_all(query=query)
    return result

async def get_tag(tag_id: int):
    query = "SELECT * FROM tag WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": tag_id})

async def create_tag(tag: Tag):
    query = """
    INSERT INTO tag (tag, description, created_by)
    VALUES (:tag, :description, :created_by)
    """
    values = {
        "tag": tag.tag,
        "description": tag.description,
        "created_by": tag.created_by,
    }
    await database.execute(query=query, values=values)

async def update_tag(tag_id: int, tag: Tag):
    query = """
    UPDATE tag
    SET tag = :tag, description = :description, created_by = :created_by,
        last_modified_date = :last_modified_date
    WHERE id = :id
    """
    values = {**tag.dict(), "id": tag_id}
    await database.execute(query=query, values=values)

async def delete_tag(tag_id: int):
    query = "DELETE FROM tag WHERE id = :id"
    await database.execute(query=query, values={"id": tag_id})
