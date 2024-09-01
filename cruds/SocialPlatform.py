from config.database import database
from models.SocialPlatform import SocialPlatform

async def get_all_social_platforms():
    query = "SELECT * FROM social_platform"
    result = await database.fetch_all(query=query)
    return result

async def get_social_platform(platform_id: int):
    query = "SELECT * FROM social_platform WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": platform_id})

async def create_social_platform(platform: SocialPlatform):
    query = """
    INSERT INTO social_platform (platform_name, is_default, logo_image, created_by)
    VALUES (:platform_name, :is_default, :logo_image, :created_by)
    """
    values = {
        "platform_name": platform.platform_name,
        "is_default": platform.is_default,
        "logo_image": platform.logo_image,
        "created_by": platform.created_by,
    }
    await database.execute(query=query, values=values)

async def update_social_platform(platform_id: int, platform: SocialPlatform):
    query = """
    UPDATE social_platform
    SET platform_name = :platform_name, is_default = :is_default, 
        logo_image = :logo_image
    WHERE id = :id
    """
    values = {
        "platform_name": platform.platform_name,
        "is_default": platform.is_default,
        "logo_image": platform.logo_image,
         "id": platform_id
         }
    await database.execute(query=query, values=values)

async def delete_social_platform(platform_id: int):
    query = "DELETE FROM social_platform WHERE id = :id"
    await database.execute(query=query, values={"id": platform_id})
