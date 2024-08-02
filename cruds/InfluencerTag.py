from config.database import database
from models.InfluencerTag import InfluencerTag

async def get_all_influencer_tags():
    query = "SELECT * FROM influencer_tag"
    result = await database.fetch_all(query=query)
    return result

async def get_influencer_tag(tag_id: int):
    query = "SELECT * FROM influencer_tag WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": tag_id})

async def create_influencer_tag(influencer_tag: InfluencerTag):
    query = """
    INSERT INTO influencer_tag (influencer_id, tag_id, created_by)
    VALUES (:influencer_id, :tag_id, :created_by)
    """
    values = {
        "influencer_id": influencer_tag.influencer_id,
        "tag_id": influencer_tag.tag_id,
        "created_by": influencer_tag.created_by,
    }
    await database.execute(query=query, values=values)

async def update_influencer_tag(tag_id: int, influencer_tag: InfluencerTag):
    query = """
    UPDATE influencer_tag
    SET influencer_id = :influencer_id, tag_id = :tag_id, created_by = :created_by,
        last_modified_date = :last_modified_date
    WHERE id = :id
    """
    values = {**influencer_tag.dict(), "id": tag_id}
    await database.execute(query=query, values=values)

async def delete_influencer_tag(tag_id: int):
    query = "DELETE FROM influencer_tag WHERE id = :id"
    await database.execute(query=query, values={"id": tag_id})
