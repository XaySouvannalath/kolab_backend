from config.database import database
from models.ImageResource import ImageResource

async def get_all_image_resources():
    query = "SELECT * FROM image_resource"
    result = await database.fetch_all(query=query)
    return result

async def get_image_resource(image_resource_id: int):
    query = "SELECT * FROM image_resource WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": image_resource_id})

async def create_image_resource(image_resource: ImageResource):
    query = """
    INSERT INTO image_resource (image_name, original_name, created_by)
    VALUES (:image_name, :original_name, :created_by)
    """
    values = {
        "image_name": image_resource.image_name,
        "original_name": image_resource.original_name,
        "created_by": image_resource.created_by,
    }
    await database.execute(query=query, values=values)

async def update_image_resource(image_resource_id: int, image_resource: ImageResource):
    query = """
    UPDATE image_resource
    SET image_name = :image_name, original_name = :original_name, created_by = :created_by, 
        last_modified_date = :last_modified_date
    WHERE id = :id
    """
    values = {**image_resource.dict(), "id": image_resource_id}
    await database.execute(query=query, values=values)

async def delete_image_resource(image_resource_id: int):
    query = "DELETE FROM image_resource WHERE id = :id"
    await database.execute(query=query, values={"id": image_resource_id})
