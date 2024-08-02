from config.database import database
from models.ReviewInsight import ReviewInsight

async def get_all_review_insights():
    query = "SELECT * FROM review_insight"
    result = await database.fetch_all(query=query)
    return result

async def get_review_insight(review_insight_id: int):
    query = "SELECT * FROM review_insight WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": review_insight_id})

async def create_review_insight(review_insight: ReviewInsight):
    query = """
    INSERT INTO review_insight (review_id, power_id, amount, rate, created_by)
    VALUES (:review_id, :power_id, :amount, :rate, :created_by)
    """
    values = {
        "review_id": review_insight.review_id,
        "power_id": review_insight.power_id,
        "amount": review_insight.amount,
        "rate": review_insight.rate,
        "created_by": review_insight.created_by,
    }
    await database.execute(query=query, values=values)

async def update_review_insight(review_insight_id: int, review_insight: ReviewInsight):
    query = """
    UPDATE review_insight
    SET review_id = :review_id, power_id = :power_id, amount = :amount, rate = :rate, 
        created_by = :created_by, last_modified_date = :last_modified_date
    WHERE id = :id
    """
    values = {**review_insight.dict(), "id": review_insight_id}
    await database.execute(query=query, values=values)

async def delete_review_insight(review_insight_id: int):
    query = "DELETE FROM review_insight WHERE id = :id"
    await database.execute(query=query, values={"id": review_insight_id})
