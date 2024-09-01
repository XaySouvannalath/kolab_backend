from config.database import database
from models.Province import Province

async def get_all_provinces():
    query = "SELECT * FROM province order by row_order asc"
    result = await database.fetch_all(query=query)
    return result

async def get_province(province_id: int):
    query = "SELECT * FROM province WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": province_id})

async def create_province(province: Province):
    query = """
    INSERT INTO province (name, description)
    VALUES (:name, :description)
    """
    values = {
        "name": province.name,
        "description": province.description
    }
    await database.execute(query=query, values=values)

async def update_province(province_id: int, province: Province):
    query = """
    UPDATE province
    SET name = :name, description = :description
    WHERE id = :id
    """
    values = {
        "nane": province.name,
        "description": province.description
        , "id": province_id}
    await database.execute(query=query, values=values)

async def delete_province(province_id: int):
    query = "DELETE FROM province WHERE id = :id"
    await database.execute(query=query, values={"id": province_id})
