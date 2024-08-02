from config.database import database
from models.AgencyInfluencer import AgencyInfluencer

from typing import List
async def get_all_agency_influencers():
    query = "SELECT * FROM agency_influencer"
    result = await database.fetch_all(query=query)
    return result

async def get_agency_influencer(agency_influencer_id: int):
    query = "SELECT * FROM agency_influencer WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": agency_influencer_id})

async def create_agency_influencer(agency_influencer: AgencyInfluencer):
    query = """
    INSERT INTO agency_influencer (agency_id, influencer_id, created_by)
    VALUES (:agency_id, :influencer_id, :created_by)
    """
    values = {
        "agency_id": agency_influencer.agency_id,
        "influencer_id": agency_influencer.influencer_id,
        "created_by": agency_influencer.created_by,
    }
    await database.execute(query=query, values=values)

async def update_agency_influencer(agency_influencer_id: int, agency_influencer: AgencyInfluencer):
    query = """
    UPDATE agency_influencer
    SET agency_id = :agency_id, influencer_id = :influencer_id, created_by = :created_by, 
        last_modified_date = :last_modified_date
    WHERE id = :id
    """
    values = {**agency_influencer.dict(), "id": agency_influencer_id}
    await database.execute(query=query, values=values)

async def delete_agency_influencer(agency_influencer_id: int):
    query = "DELETE FROM agency_influencer WHERE id = :id"
    await database.execute(query=query, values={"id": agency_influencer_id})



#additional

async def get_agency_influencers_by_agency_id(agency_id: int) -> List[AgencyInfluencer]:
    query = """
    SELECT * FROM `agency_influencer` WHERE agency_id = :agency_id
    """
    result = await database.fetch_all(query=query, values={"agency_id": agency_id})
    return [AgencyInfluencer(**row) for row in result]

async def get_agency_influencers_by_influencer_id(influencer_id: int) -> List[AgencyInfluencer]:
    query = """
    SELECT * FROM `agency_influencer` WHERE influencer_id = :influencer_id
    """
    result = await database.fetch_all(query=query, values={"influencer_id": influencer_id})
    return [AgencyInfluencer(**row) for row in result]