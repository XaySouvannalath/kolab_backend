from config.database import database
from models.Power import Power

async def get_all_powers():
    query = "SELECT * FROM power"
    result = await database.fetch_all(query=query)
    return result

async def get_power(power_id: int):
    query = "SELECT * FROM power WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": power_id})

async def create_power(power: Power):
    query = """
    INSERT INTO power (power, description, created_by)
    VALUES (:power, :description, :created_by)
    """
    values = {
        "power": power.power,
        "description": power.description,
        "created_by": power.created_by,
    }
    await database.execute(query=query, values=values)

async def update_power(power_id: int, power: Power):
    query = """
    UPDATE power
    SET power = :power, description = :description
    WHERE id = :id
    """
    values = {
        "power": power.power,
        "description": power.description
        , "id": power_id}
    await database.execute(query=query, values=values)

async def delete_power(power_id: int):
    query = "DELETE FROM power WHERE id = :id"
    await database.execute(query=query, values={"id": power_id})
