from fastapi import HTTPException
from config.database import database
from models.InfluencerTag import InfluencerTag
from models.InfluencerTagResponse import InfluencerTagModel, InfluencerTagsResponse

async def get_all_influencer_tags():
    query = """
    select a.* , c.channel_name, b.tag
    from influencer_tag a
    
    inner join influencer c on c.id = a.influencer_id
    inner join tag b on b.id = a.tag_id
    
    """
    result = await database.fetch_all(query=query)
    return result

# select pure tag detail by influencer_id
async def get_influencer_tags_v3(influencer_id: int):
    tags_query = """
        SELECT it.id as influencer_tag_id, t.tag, t.color
        FROM influencer_tag it
        inner JOIN tag t ON it.tag_id = t.id
        WHERE it.influencer_id = :influencer_id
        """
    tags = await database.fetch_all(query=tags_query, values={"influencer_id": influencer_id})
    return tags

async def get_influencer_tags_v2():
    # Step 1: Get all influencers
    influencer_query = """
    SELECT id, channel_name  
    FROM influencer
    """
    influencers = await database.fetch_all(query=influencer_query)

    if not influencers:
        raise HTTPException(status_code=404, detail="No influencers found.")

    influencer_responses = []

    # Step 2: Loop through each influencer to get their tags
    for influencer in influencers:
        influencer_id = influencer["id"]
        channel_name = influencer["channel_name"]

        # Fetch associated tags for the current influencer
        tags_query = """
        SELECT it.id as influencer_tag_id, t.tag, t.color
        FROM influencer_tag it
        inner JOIN tag t ON it.tag_id = t.id
        WHERE it.influencer_id = :influencer_id
        """
        tags = await database.fetch_all(query=tags_query, values={"influencer_id": influencer_id})

        # Map the tags into a list of InfluencerTagModel
        tag_models = [InfluencerTagModel(influencer_tag_id=tag["influencer_tag_id"], tag=tag["tag"], color=tag["color"]) for tag in tags]

        # Add the influencer and their tags to the response list
        influencer_responses.append(
            InfluencerTagsResponse(
                influencer_id=influencer_id,
                channel_name=channel_name,
                tags=tag_models
            )
        )

    return influencer_responses

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
