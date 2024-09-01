from datetime import date
from typing import List
from config.database import database
from models.FollowerLog import FollowerLog

async def get_all_follower_logs():
    query = "SELECT * FROM follower_logs"
    result = await database.fetch_all(query=query)
    return result

async def get_follower_log(follower_log_id: int):
    query = "SELECT * FROM follower_logs WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": follower_log_id})

async def create_follower_log(follower_log: FollowerLog):
    query = """
    INSERT INTO follower_logs (influencer_id, platform_id, num_of_follower)
    VALUES (:influencer_id, :platform_id, :num_of_follower)
    """
    values = {
        "influencer_id": follower_log.influencer_id,
        "platform_id": follower_log.platform_id,
        "num_of_follower": follower_log.num_of_follower,

    }
    await database.execute(query=query, values=values)

async def update_follower_log(follower_log_id: int, follower_log: FollowerLog):
    query = """
    UPDATE follower_logs
    SET influencer_id = :influencer_id, platform_id = :platform_id, profile_url = :profile_url, 
        num_of_follower = :num_of_follower, as_of_date = :as_of_date, created_by = :created_by,
        last_modified_date = :last_modified_date
    WHERE id = :id
    """
    values = {**follower_log.dict(), "id": follower_log_id}
    await database.execute(query=query, values=values)

async def delete_follower_log(follower_log_id: int):
    query = "DELETE FROM follower_logs WHERE id = :id"
    await database.execute(query=query, values={"id": follower_log_id})


async def get_follower_logs_by_influencer_id_and_date_range(
    influencer_id: int,
    start_date: date,
    end_date: date
) -> List[FollowerLog]:
    query = """
    SELECT * FROM follower_logs
    WHERE influencer_id = :influencer_id
      AND as_of_date BETWEEN :start_date AND :end_date
    """
    result = await database.fetch_all(
        query=query,
        values={"influencer_id": influencer_id, "start_date": start_date, "end_date": end_date}
    )
    return [FollowerLog(**row) for row in result]