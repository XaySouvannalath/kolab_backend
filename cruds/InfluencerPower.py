from config.database import database
from models.InfluencerPower import InfluencerPower
from typing import List

async def get_all_influencer_powers():
    query = "SELECT * FROM influencer_power"
    result = await database.fetch_all(query=query)
    return result

async def get_influencer_power(influencer_power_id: int):
    query = "SELECT * FROM influencer_power WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": influencer_power_id})

async def create_influencer_power(influencer_power: InfluencerPower):
    query = """
    INSERT INTO influencer_power (influencer_id, power_id, amount, rate, created_by)
    VALUES (:influencer_id, :power_id, :amount, :rate, :created_by)
    """
    values = {
        "influencer_id": influencer_power.influencer_id,
        "power_id": influencer_power.power_id,
        "amount": influencer_power.amount,
        "rate": influencer_power.rate,
        "created_by": influencer_power.created_by,
    }
    await database.execute(query=query, values=values)

async def update_influencer_power(influencer_power_id: int, influencer_power: InfluencerPower):
    query = """
    UPDATE influencer_power
    SET influencer_id = :influencer_id, power_id = :power_id, amount = :amount, 
        rate = :rate, created_by = :created_by, last_modified_date = :last_modified_date
    WHERE id = :id
    """
    values = {**influencer_power.dict(), "id": influencer_power_id}
    await database.execute(query=query, values=values)

async def delete_influencer_power(influencer_power_id: int):
    query = "DELETE FROM influencer_power WHERE id = :id"
    await database.execute(query=query, values={"id": influencer_power_id})

async def get_influencer_powers_by_influencer_id(influencer_id: int) -> List[InfluencerPower]:
    query = """
    SELECT * FROM influencer_power
    WHERE influencer_id = :influencer_id
    """
    result = await database.fetch_all(
        query=query,
        values={"influencer_id": influencer_id}
    )
    return [InfluencerPower(**row) for row in result]