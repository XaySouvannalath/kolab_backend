from datetime import datetime

from config.database import database
from models.Achievement import InfluencerAchievement

# Get all achievements
async def get_all_achievements():
    query = "SELECT * FROM influencer_achievement"
    result = await database.fetch_all(query=query)
    return result

# Get achievement by ID
async def get_achievement(achievement_id: int):
    query = "SELECT * FROM influencer_achievement WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": achievement_id})

# Get all achievements of a specific influencer
async def get_achievement_by_influencer_id(influencer_id: int):
    query = "SELECT * FROM influencer_achievement WHERE influencer_id = :influencer_id"
    return await database.fetch_all(query=query, values={"influencer_id": influencer_id})

# Create new achievement
async def create_achievement(achievement: InfluencerAchievement):
    print("Create achievement")
    query = """
    INSERT INTO influencer_achievement (influencer_id, achievement_text)
    VALUES (:influencer_id, :achievement_text)
    """
    values = {
        "influencer_id": achievement.influencer_id,
        "achievement_text": achievement.achievement_text
    }
    await database.execute(query=query, values=values)
    print("Data for inserting")
    print(values)

# Update achievement
async def update_achievement(achievement_id: int, achievement: InfluencerAchievement):
    query = """
    UPDATE influencer_achievement
    SET influencer_id = :influencer_id,
        achievement_text = :achievement_text
    WHERE id = :id
    """
    values = {
        "influencer_id": achievement.influencer_id,
        "achievement_text": achievement.achievement_text,
        "id": achievement_id
    }
    await database.execute(query=query, values=values)

# Delete achievement
async def delete_achievement(achievement_id: int):
    query = "DELETE FROM influencer_achievement WHERE id = :id"
    await database.execute(query=query, values={"id": achievement_id})
