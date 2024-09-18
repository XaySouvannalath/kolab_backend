from config.database import database
from models.InfluencerSearchCondition import InfluencerSearchCondition
from models.Influencer import Influencer

from cruds.InfluencerTag import get_influencer_tags_v3
from cruds.InfluencerSocialAccount import *
from models.InfluencerSocialAccount import InfluencerSocialAccount
from models.InfluencerTagResponse import InfluencerTagModel

async def get_all_influencers():
    query = """
    
    select a.* , b.name as content_style, c.name as province_name, c.description as province_description,
    d.agency_name as agency_name, e.description as birth_place_description
    
    from influencer a 
    inner join content_style b on b.id = a.content_style_id
    left join province c on c.id = a.province_id
    left join agency d on d.id = a.agency_id
    
    left join province e on e.id = a.birth_place
    """
    result = await database.fetch_all(query=query)
    return result

async def get_influencer(influencer_id: int):
    query = "SELECT * FROM influencer WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": influencer_id})

async def create_influencer(influencer: Influencer):
    query = """
    INSERT INTO influencer (channel_name, content_style_id, is_available, first_name, last_name, nick_name, remark, 
                            date_of_birth, has_agency, created_by, gender, agency_id, photo, province_id,
                            birth_place, impression, reach, engagement)
    VALUES (:channel_name, :content_style_id, :is_available, :first_name, :last_name, :nick_name, :remark, 
            :date_of_birth, :has_agency, :created_by, :gender, :agency_id, :photo, :province_id,
            :birth_place, :impression, :reach, :engagement
            
            )
    """
    values = {
        "channel_name": influencer.channel_name,
        "content_style_id": influencer.content_style_id,
        "is_available": influencer.is_available,
        "first_name": influencer.first_name,
        "last_name": influencer.last_name,
        "nick_name": influencer.nick_name,
        "remark": influencer.remark,
        "date_of_birth": influencer.date_of_birth,
        "has_agency": influencer.has_agency,
        "created_by": influencer.created_by,
        "gender": influencer.gender,
        "agency_id": influencer.agency_id,
        "photo": influencer.photo,
        "province_id": influencer.province_id,
        "birth_place": influencer.birth_place,
        "impression": influencer.impression,
        "reach": influencer.reach,
        "engagement": influencer.engagement
    }
    await database.execute(query=query, values=values)

async def update_influencer(influencer_id: int, influencer: Influencer):
    query = """
    UPDATE influencer
    SET channel_name = :channel_name, content_style_id = :content_style_id, is_available = :is_available, 
        first_name = :first_name, last_name = :last_name, nick_name = :nick_name, remark = :remark,
        date_of_birth = :date_of_birth, has_agency = :has_agency, gender = :gender, agency_id = :agency_id, 
        photo = :photo, province_id = :province_id, birth_place = :birth_place,
        impression = :impression, reach = :reach, engagement = :engagement
    WHERE id = :id
    """
    values = {
        "channel_name": influencer.channel_name,
        "content_style_id": influencer.content_style_id,
        "is_available": influencer.is_available,
        "first_name": influencer.first_name,
        "last_name": influencer.last_name,
        "nick_name": influencer.nick_name,
        "remark": influencer.remark,
        "date_of_birth": influencer.date_of_birth,
        "has_agency": influencer.has_agency,
        "gender": influencer.gender,
        "agency_id": influencer.agency_id,
        "photo": influencer.photo,
        "province_id": influencer.province_id,
        "birth_place": influencer.birth_place,
        "impression": influencer.impression,
        "reach": influencer.reach,
        "engagement": influencer.engagement,
        "id": influencer_id
    }
    await database.execute(query=query, values=values)


async def delete_influencer(influencer_id: int):
    query = "DELETE FROM influencer WHERE id = :id"
    await database.execute(query=query, values={"id": influencer_id})



async def search_influencer(conditions: InfluencerSearchCondition):
    query = """
    select a.* , b.name as content_style, c.name as province_name, c.description as province_description,
    d.agency_name, e.description as birth_place_description
    from influencer a 
    inner join content_style b on b.id = a.content_style_id
    left join province c on c.id = a.province_id
    left join agency d on d.id = a.agency_id
  
    left join province e on e.id = a.birth_place
    where 1 = 1
    """
 
    print(conditions)
   # Append conditions if they are not None
    if conditions.id is not None:
        query += f" AND a.id = {conditions.id}"
    # if conditions.channel_name:
    #     query += f" AND a.channel_name LIKE '%{conditions.channel_name}%'"
    # if conditions.first_name:
    #     query += f" AND a.first_name LIKE '%{conditions.first_name}%'"
    # if conditions.last_name:
    #     query += f" AND a.last_name LIKE '%{conditions.last_name}%'"
    # if conditions.province_id is not None:
    #     query += f" AND a.province_id = {conditions.province_id}"
    # if conditions.content_style_id is not None:
    #     query += f" AND a.content_style_id = {conditions.content_style_id}"
        
    # version 2
    # Check for keyword condition
    if conditions.keyword:
        keyword = f"%{conditions.keyword}%"  # Wildcard search
        query += f"""
        AND (
            a.id = '{conditions.keyword}'
            OR a.channel_name LIKE '{keyword}'
            OR a.first_name LIKE '{keyword}'
            OR a.last_name LIKE '{keyword}'
        )
        """
    
     # Filter by province_id if a list is provided
    if conditions.province_id:
        province_ids = ','.join(map(str, conditions.province_id))
        query += f" AND a.province_id IN ({province_ids})"

    # Filter by content_style_id if a list is provided
    if conditions.content_style_id:
        content_style_ids = ','.join(map(str, conditions.content_style_id))
        query += f" AND a.content_style_id IN ({content_style_ids})"
    
    # Filter by tag_id if a list is provided
    if conditions.tag_id:
        tag_ids = ','.join(map(str, conditions.tag_id))
        query += f""" AND EXISTS (
                        SELECT 1
                        FROM influencer_tag it
                        WHERE it.influencer_id = a.id
                        AND it.tag_id IN ({tag_ids})  
        )"""
        
    if conditions.social_platform_id:
        social_platform_ids = ','.join(map(str, conditions.social_platform_id))
        query += f"""
         and a.id in (
            SELECT DISTINCT  fl.influencer_id
            FROM follower_logs fl
            INNER JOIN (
                SELECT influencer_id, MAX(created_date) AS created_date
                FROM follower_logs
                GROUP BY influencer_id
            ) latest ON fl.influencer_id = latest.influencer_id AND 
            fl.created_date = latest.created_date and fl.platform_id in ({social_platform_ids})
            and fl.num_of_follower {conditions.number_of_follower}

         )
        """
    
    print(query)
    result = await database.fetch_all(query=query)
    
    influencer_response = []
    for r in result:
        tags = await get_influencer_tags_v3(r.id)
        tag_models = []
        for tag in tags:
            # print(tag.tag)
            influencer_tag_model = InfluencerTagModel(
                influencer_tag_id=r["id"],
                tag=tag["tag"],
                color=tag["color"]
            )
            tag_models.append(influencer_tag_model)
        
        
        social_accounts = await get_social_accounts_by_influencer_id(influencer_id=r["id"])
        
        sa_models = []
        for sa in social_accounts:
            sa_model = InfluencerSocialAccount(
                id=sa["id"],
                num_of_follower=sa["num_of_follower"],
                platform_name=sa["platform_name"],
                logo_image=sa["logo_image"]
                
            )
            sa_models.append(sa_model)
            
        influencer_response.append(
            Influencer(
                    id=r["id"],
                    channel_name=r["channel_name"],
                    content_style_id=r["content_style_id"],
                    content_style = r["content_style"],
                    is_available=r["is_available"],
                    first_name=r["first_name"],
                    last_name=r["last_name"],
                    nick_name=r["nick_name"],
                    remark=r["remark"],
                    date_of_birth=r["date_of_birth"],
                    has_agency=r["has_agency"],
                    created_date=r["created_date"],
                    created_by=r["created_by"],
                    last_modified_date=r["last_modified_date"],
                    gender=r["gender"],
                    agency_id=r["agency_id"],
                    photo=r["photo"],
                    province_id=r["province_id"],
                    province_description=r["province_description"],
                    agency_name=r['agency_name'],
                    birth_place=r['birth_place'],
                    birth_place_description=r['birth_place_description'],
                    impression=r['impression'],
                    reach=r['reach'],
                    engagement=r['engagement'],
                    tags=tag_models,
                    social_accounts=sa_models
                ) 
            )
        
    return influencer_response
    
    