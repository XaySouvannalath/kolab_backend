from typing import Union
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from models.Agency import Item, Agency
from setting.dbrun import connect

from cruds.agency import *
router = APIRouter(
    prefix="/agency"
)





@router.get("/", tags=["agency"])
async def get(id: Union[str, None] = None):
    print()
    result = {}
    if id is not None:
        result = await get_agency_one(id)
        if result is None:
            raise HTTPException(status_code=404, detail="Agency not found")
    else:
      result = await get_all_agency()
      if result is None:
          raise HTTPException(status_code=404, detail="Agency not found")
    return result



 

@router.post("/", tags=["agency"])
async def create(agency: Agency):
    await create_agency(agency)
    return agency

@router.put("/{agency_id}", response_model=Agency, tags=["agency"])
async def update(agency_id: int, agency: Agency):
    existing_agency = await get_agency(agency_id)
    if existing_agency is None:
        raise HTTPException(status_code=404, detail="Agency not found")
    await update_agency(agency_id, agency)
    return agency


@router.delete("/{agency_id}", response_model=Agency, tags=["agency"])
async def delete(agency_id: int):
    existing_agency = await get_agency(agency_id)
    if existing_agency is None:
        raise HTTPException(status_code=404, detail="Agency not found")
    await delete_agency(agency_id)
    return existing_agency
