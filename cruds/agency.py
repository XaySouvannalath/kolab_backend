from datetime import datetime

from config.database import database
from models.Agency import Agency

async def get_all_agency():
    query = "SELECT * FROM agency"
    result =  await database.fetch_all(query=query)

    return result
async def get_agency(agency_id: int):
    query = "SELECT * FROM agency WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": agency_id})

async def get_agency_one(id):
    
    query= "SELECT * FROM agency where id = :id"
    print(query)
    result =  await database.fetch_one(query=query,values={"id": id})
    return result

# async def insert_agency(agency: Agency):
async def create_agency(agency: Agency):
    print("Create agency")
    query = """
    INSERT INTO agency (agency_name, telephone, email, address)
    VALUES (:agency_name, :telephone, :email, :address)
    """
    values = {
        "agency_name": agency.agency_name,
        "telephone": agency.telephone,
        "email": agency.email,
        "address": agency.address
    }
    await database.execute(query=query, values=values)
    
    print("Data for inserting")
    print(values)
    await database.execute(query=query, values=values)

async def get_agency(agency_id: int):
    query = "SELECT * FROM agency WHERE id = :id"
    return await database.fetch_one(query=query, values={"id": agency_id})

async def update_agency(agency_id: int, agency: Agency):
    query = """
    UPDATE agency
    SET agency_name = :agency_name, telephone = :telephone, email = :email, address = :address
        
    WHERE id = :id
    """
    values = {
        "agency_name": agency.agency_name,
        "telephone": agency.telephone,
        "email": agency.email,
        "address": agency.address
        , "id": agency_id}
    await database.execute(query=query, values=values)

async def delete_agency(agency_id: int):
    query = "DELETE FROM agency WHERE id = :id"
    await database.execute(query=query, values={"id": agency_id})