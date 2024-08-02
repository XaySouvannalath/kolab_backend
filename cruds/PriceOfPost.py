from config.database import database
from models.PriceOfPost import PriceOfPost

async def get_all_prices():
    query = "SELECT * FROM price_of_post"
    result = await database.fetch_all(query=query)
    return result

async def get_price(price_id: int):
    query = "SELECT * FROM price_of_post WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": price_id})

async def create_price(price: PriceOfPost):
    query = """
    INSERT INTO price_of_post (type_of_post_id, influencer_id, price, created_by)
    VALUES (:type_of_post_id, :influencer_id, :price, :created_by)
    """
    values = {
        "type_of_post_id": price.type_of_post_id,
        "influencer_id": price.influencer_id,
        "price": price.price,
        "created_by": price.created_by,
    }
    await database.execute(query=query, values=values)

async def update_price(price_id: int, price: PriceOfPost):
    query = """
    UPDATE price_of_post
    SET type_of_post_id = :type_of_post_id, influencer_id = :influencer_id, price = :price,
        created_by = :created_by, last_modified_date = :last_modified_date
    WHERE id = :id
    """
    values = {**price.dict(), "id": price_id}
    await database.execute(query=query, values=values)

async def delete_price(price_id: int):
    query = "DELETE FROM price_of_post WHERE id = :id"
    await database.execute(query=query, values={"id": price_id})
