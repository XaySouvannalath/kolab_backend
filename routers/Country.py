from typing import Union
from fastapi import APIRouter, HTTPException
from models.Country import Country
from cruds.Country import *

router = APIRouter(
    prefix="/countries"
)

@router.get("/", tags=["countries"])
async def get(id: Union[str, None] = None):
    if id is not None:
        result = await get_country(int(id))
        if result is None:
            raise HTTPException(status_code=404, detail="Country not found")
    else:
        result = await get_all_countries()
        if not result:
            raise HTTPException(status_code=404, detail="No countries found")
    return result

@router.post("/", tags=["countries"])
async def create(country: Country):
    await create_country(country)
    return country

@router.put("/{country_id}", response_model=Country, tags=["countries"])
async def update(country_id: int, country: Country):
    existing_country = await get_country(country_id)
    if existing_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    await update_country(country_id, country)
    return country

@router.delete("/{country_id}", response_model=Country, tags=["countries"])
async def delete(country_id: int):
    existing_country = await get_country(country_id)
    if existing_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    await delete_country(country_id)
    return existing_country