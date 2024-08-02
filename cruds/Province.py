from config.database import database
from models.Province import Province

async def get_all_provinces():
    query = "SELECT * FROM province"
    result = await database.fetch_all(query=query)
    return result

async def get_province(province_id: int):
    query = "SELECT * FROM province WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": province_id})

async def create_province(province: Province):
    query = """
    INSERT INTO province (name, description, created_by)
    VALUES (:name, :description, :created_by)
    """
    values = {
        "name": province.name,
        "description": province.description,
        "created_by": province.created_by,
    }
    await database.execute(query=query, values=values)

async def update_province(province_id: int, province: Province):
    query = """
    UPDATE province
    SET name = :name, description = :description, created_by = :created_by,
        last_modified_date = :last_modified_date
    WHERE id = :id
    """
    values = {**province.dict(), "id": province_id}
    await database.execute(query=query, values=values)

async def delete_province(province_id: int):
    query = "DELETE FROM province WHERE id = :id"
    await database.execute(query=query, values={"id": province_id})
