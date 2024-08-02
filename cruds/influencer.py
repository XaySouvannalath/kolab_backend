from config.database import database
from models.Influencer import Influencer

async def get_all_influencers():
    query = "SELECT * FROM influencer"
    result = await database.fetch_all(query=query)
    return result

async def get_influencer(influencer_id: int):
    query = "SELECT * FROM influencer WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": influencer_id})

async def create_influencer(influencer: Influencer):
    query = """
    INSERT INTO influencer (channel_name, content_style, is_available, first_name, last_name, nick_name, remark, 
                            date_of_birth, has_agency, created_by, gender)
    VALUES (:channel_name, :content_style, :is_available, :first_name, :last_name, :nick_name, :remark, 
            :date_of_birth, :has_agency, :created_by, :gender)
    """
    values = {
        "channel_name": influencer.channel_name,
        "content_style": influencer.content_style,
        "is_available": influencer.is_available,
        "first_name": influencer.first_name,
        "last_name": influencer.last_name,
        "nick_name": influencer.nick_name,
        "remark": influencer.remark,
        "date_of_birth": influencer.date_of_birth,
        "has_agency": influencer.has_agency,
        "created_by": influencer.created_by,
        "gender": influencer.gender,
    }
    await database.execute(query=query, values=values)

async def update_influencer(influencer_id: int, influencer: Influencer):
    query = """
    UPDATE influencer
    SET channel_name = :channel_name, content_style = :content_style, is_available = :is_available, 
        first_name = :first_name, last_name = :last_name, nick_name = :nick_name, remark = :remark,
        date_of_birth = :date_of_birth, has_agency = :has_agency, created_date = :created_date, 
        created_by = :created_by, last_modified_date = :last_modified_date, gender = :gender
    WHERE id = :id
    """
    values = {**influencer.dict(), "id": influencer_id}
    await database.execute(query=query, values=values)

async def delete_influencer(influencer_id: int):
    query = "DELETE FROM influencer WHERE id = :id"
    await database.execute(query=query, values={"id": influencer_id})
