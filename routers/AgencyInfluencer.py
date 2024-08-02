from typing import Union
from fastapi import APIRouter, HTTPException
from models.AgencyInfluencer import AgencyInfluencer
from cruds.AgencyInfluencer import *

router = APIRouter(
    prefix="/agency_influencer"
)

@router.get("/", tags=["agency_influencer"])
async def get(id: Union[str, None] = None):
    result = {}
    if id is not None:
        result = await get_agency_influencer(id)
        if result is None:
            raise HTTPException(status_code=404, detail="AgencyInfluencer not found")
    else:
        result = await get_all_agency_influencers()
        if result is None:
            raise HTTPException(status_code=404, detail="AgencyInfluencers not found")
    return result

@router.post("/", tags=["agency_influencer"])
async def create(agency_influencer: AgencyInfluencer):
    await create_agency_influencer(agency_influencer)
    return agency_influencer

@router.put("/{agency_influencer_id}", response_model=AgencyInfluencer, tags=["agency_influencer"])
async def update(agency_influencer_id: int, agency_influencer: AgencyInfluencer):
    existing_agency_influencer = await get_agency_influencer(agency_influencer_id)
    if existing_agency_influencer is None:
        raise HTTPException(status_code=404, detail="AgencyInfluencer not found")
    await update_agency_influencer(agency_influencer_id, agency_influencer)
    return agency_influencer

@router.delete("/{agency_influencer_id}", response_model=AgencyInfluencer, tags=["agency_influencer"])
async def delete(agency_influencer_id: int):
    existing_agency_influencer = await get_agency_influencer(agency_influencer_id)
    if existing_agency_influencer is None:
        raise HTTPException(status_code=404, detail="AgencyInfluencer not found")
    await delete_agency_influencer(agency_influencer_id)
    return existing_agency_influencer


#additional

@router.get("/agency/{agency_id}", response_model=List[AgencyInfluencer], tags=["agency_influencer"])
async def get_by_agency_id(agency_id: int):
    agency_influencers = await get_agency_influencers_by_agency_id(agency_id)
    if not agency_influencers:
        raise HTTPException(status_code=404, detail="No influencers found for this agency")
    return agency_influencers

@router.get("/influencer/{influencer_id}", response_model=List[AgencyInfluencer], tags=["agency_influencer"])
async def get_by_influencer_id(influencer_id: int):
    agency_influencers = await get_agency_influencers_by_influencer_id(influencer_id)
    if not agency_influencers:
        raise HTTPException(status_code=404, detail="No agencies found for this influencer")
    return agency_influencers