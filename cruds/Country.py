from config.database import database
from models.Country import Country

async def get_all_countries():
    query = "SELECT * FROM country where rs = 'O' ORDER BY row_order ASC"
    result = await database.fetch_all(query=query)
    return result

async def get_country(country_id: int):
    query = "SELECT * FROM country WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": country_id})

async def create_country(country: Country):
    query = """
    INSERT INTO country (country_name, description, created_by, row_order)
    VALUES (:country_name, :description, :created_by, :row_order)
    """
    values = {
        "country_name": country.country_name,
        "description": country.description,
        "created_by": country.created_by,
        "row_order": country.row_order
    }
    await database.execute(query=query, values=values)

async def update_country(country_id: int, country: Country):
    query = """
    UPDATE country
    SET country_name = :country_name, description = :description, 
        created_by = :created_by, row_order = :row_order
    WHERE id = :id
    """
    values = {
        "country_name": country.country_name,
        "description": country.description,
        "created_by": country.created_by,
        "row_order": country.row_order,
        "id": country_id
    }
    await database.execute(query=query, values=values)

async def delete_country(country_id: int):
    query = "DELETE FROM country WHERE id = :id"
    await database.execute(query=query, values={"id": country_id})