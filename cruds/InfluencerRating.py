from config.database import database
from models.InfluencerRating import InfluencerRating

async def get_influencer_ratings(influencer_id: int):
    query = """
    SELECT ir.id,
           ir.influencer_id,
           ir.rating_id,
           r.category,
           ir.score,
           ir.created_date,
           ir.created_by,
           ir.last_modified_date
    FROM influencer_rating ir
    INNER JOIN rating r ON ir.rating_id = r.id
    WHERE ir.influencer_id = :influencer_id
    """
    values = {"influencer_id": influencer_id}
    results = await database.fetch_all(query=query, values=values)
    return results