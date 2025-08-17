from config.database import database
from models.InfluencerSearchCondition import InfluencerSearchCondition
from models.Influencer import Influencer

from cruds.InfluencerTag import get_influencer_tags_v3
from cruds.InfluencerSocialAccount import *
from models.InfluencerSocialAccount import InfluencerSocialAccount
from models.InfluencerTagResponse import InfluencerTagModel

async def influencer_page():
    query = """
    select (ceil((select count(*) from influencer)/10)) as pages;
    """
    result = await database.fetch_all(query= query)
    return result[0]


async def search_influencer(conditions: InfluencerSearchCondition):
    query = """
    select a.* , b.name as content_style, c.name as province_name, c.description as province_description,
    d.agency_name, e.description as birth_place_description
    from influencer a 
    inner join content_style b on b.id = a.content_style_id
    left join province c on c.id = a.provnince_id
    left join agency d on d.id = a.agency_id
  
    left join province e on e.id = a.birth_place
    where 1 = 1
    """
 
    print(conditions)
   # Append conditions if they are not None
    if conditions.id is not None:
        query += f" AND a.id = {conditions.id}"
    
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
    
    # print(query)
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
            print(sa)
            sa_model = InfluencerSocialAccount(
                id=sa["id"],
                num_of_follower=sa["num_of_follower"],
                platform_name=sa["platform_name"],
                logo_image=sa["logo_image"],
                profile_name=sa["profile_name"],
                profile_url=sa["profile_url"],
                api_follower_link=sa["api_follower_link"],
                social_platform_id=sa["id"],
                meta_id=sa["meta_id"],
                influencer_id=r["id"]
                
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
                    social_accounts=sa_models,
                    photo2= r['photo2'],
                    photo3= r['photo3'],
                    # Add the new fields
                    is_active=r['is_active'],
                    notable_projects=r['notable_projects'],
                    # content_style is already included above
                    notable_skills=r['notable_skills'],
                    achievements=r['achievements'],
                    kolab_experienced=r['kolab_experienced']
                ) 
            )
        
    return influencer_response

