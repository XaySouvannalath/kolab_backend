from config.database import database
from models.InfluencerReview import InfluencerReview

async def get_all_influencer_reviews():
    query = "SELECT * FROM influencer_review"
    result = await database.fetch_all(query=query)
    return result

async def get_influencer_review(review_id: int):
    query = "SELECT * FROM influencer_review WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": review_id})

async def create_influencer_review(influencer_review: InfluencerReview):
    query = """
    INSERT INTO influencer_review (influencer_id, brand, campaign_name, start_at, end_at, created_by)
    VALUES (:influencer_id, :brand, :campaign_name, :start_at, :end_at, :created_by)
    """
    values = {
        "influencer_id": influencer_review.influencer_id,
        "brand": influencer_review.brand,
        "campaign_name": influencer_review.campaign_name,
        "start_at": influencer_review.start_at,
        "end_at": influencer_review.end_at,
        "created_by": influencer_review.created_by,
    }
    await database.execute(query=query, values=values)

async def update_influencer_review(review_id: int, influencer_review: InfluencerReview):
    query = """
    UPDATE influencer_review
    SET influencer_id = :influencer_id, brand = :brand, campaign_name = :campaign_name, 
        start_at = :start_at, end_at = :end_at, created_by = :created_by, 
        last_modified_date = :last_modified_date
    WHERE id = :id
    """
    values = {**influencer_review.dict(), "id": review_id}
    await database.execute(query=query, values=values)

async def delete_influencer_review(review_id: int):
    query = "DELETE FROM influencer_review WHERE id = :id"
    await database.execute(query=query, values={"id": review_id})
