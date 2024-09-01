from config.database import database
from models.PriceOfPost import PriceOfPost

async def get_all_prices():
    query = "SELECT * FROM price_of_post"
    result = await database.fetch_all(query=query)
    return result

async def get_price(price_id: int):
    query = "SELECT * FROM price_of_post WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": price_id})

async def create_price(type_of_post_id: int, influencer_id: int, price: float):
    query = """
    INSERT INTO price_of_post (type_of_post_id, influencer_id, price)
    VALUES (:type_of_post_id, :influencer_id, :price)
    """
    values = {
        "type_of_post_id": type_of_post_id,
        "influencer_id": influencer_id,
        "price": price
    }
    await database.execute(query=query, values=values)

async def update_price(price_id: int, influencer_id:int, price: float, type_of_post_id: int):
    query = """
    UPDATE price_of_post
    SET type_of_post_id = :type_of_post_id, influencer_id = :influencer_id, price = :price
    WHERE id = :id
    """

    values = {
        "type_of_post_id": type_of_post_id,
        "influencer_id": influencer_id,
        "price": price,
        "id": price_id
    }

    await database.execute(query=query, values=values)

async def delete_price(price_id: int):
    query = "DELETE FROM price_of_post WHERE id = :id"
    await database.execute(query=query, values={"id": price_id})


async def get_price_of_post_by_influencer_id(influencer_id: int):
    query = """
        select a.id, a.name, a.description,
        ifnull((select price from price_of_post where influencer_id = :influencer_id and type_of_post_id = a.id order by id desc limit 1),0) as price,
        ifnull((select id from price_of_post where influencer_id = :influencer_id and type_of_post_id = a.id order by id desc limit 1),0) as meta_id
        from posts a;
    """
    
    value = {
        "influencer_id": influencer_id,
        "influencer_id": influencer_id,
    }
    
    result = await database.fetch_all(query=query, values=value)
    return result
    
    
    