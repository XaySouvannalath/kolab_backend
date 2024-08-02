from config.database import database
from models.InfluencerAddress import InfluencerAddress

async def get_all_influencer_addresses():
    query = "SELECT * FROM influencer_address"
    result = await database.fetch_all(query=query)
    return result

async def get_influencer_address(influencer_address_id: int):
    query = "SELECT * FROM influencer_address WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": influencer_address_id})

async def create_influencer_address(influencer_address: InfluencerAddress):
    query = """
    INSERT INTO influencer_address (influencer_id, province_id, district_id, village_id, created_by)
    VALUES (:influencer_id, :province_id, :district_id, :village_id, :created_by)
    """
    values = {
        "influencer_id": influencer_address.influencer_id,
        "province_id": influencer_address.province_id,
        "district_id": influencer_address.district_id,
        "village_id": influencer_address.village_id,
        "created_by": influencer_address.created_by,
    }
    await database.execute(query=query, values=values)

async def update_influencer_address(influencer_address_id: int, influencer_address: InfluencerAddress):
    query = """
    UPDATE influencer_address
    SET influencer_id = :influencer_id, province_id = :province_id, district_id = :district_id, 
        village_id = :village_id, created_by = :created_by, last_modified_date = :last_modified_date
    WHERE id = :id
    """
    values = {**influencer_address.dict(), "id": influencer_address_id}
    await database.execute(query=query, values=values)

async def delete_influencer_address(influencer_address_id: int):
    query = "DELETE FROM influencer_address WHERE id = :id"
    await database.execute(query=query, values={"id": influencer_address_id})
