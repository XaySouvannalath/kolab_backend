from typing import Union
from fastapi import APIRouter, HTTPException
from models.FollowerLog import FollowerLog
from cruds.FollowerLog import *

router = APIRouter(
    prefix="/follower_logs"
)

@router.get("/", tags=["follower_logs"])
async def get(id: Union[str, None] = None):
    result = {}
    if id is not None:
        result = await get_follower_log(id)
        if result is None:
            raise HTTPException(status_code=404, detail="FollowerLog not found")
    else:
        result = await get_all_follower_logs()
        if result is None:
            raise HTTPException(status_code=404, detail="FollowerLogs not found")
    return result

@router.post("/", tags=["follower_logs"])
async def create(follower_log: FollowerLog):
    await create_follower_log(follower_log)
    return follower_log

@router.put("/{follower_log_id}", response_model=FollowerLog, tags=["follower_logs"])
async def update(follower_log_id: int, follower_log: FollowerLog):
    existing_follower_log = await get_follower_log(follower_log_id)
    if existing_follower_log is None:
        raise HTTPException(status_code=404, detail="FollowerLog not found")
    await update_follower_log(follower_log_id, follower_log)
    return follower_log

@router.delete("/{follower_log_id}", response_model=FollowerLog, tags=["follower_logs"])
async def delete(follower_log_id: int):
    existing_follower_log = await get_follower_log(follower_log_id)
    if existing_follower_log is None:
        raise HTTPException(status_code=404, detail="FollowerLog not found")
    await delete_follower_log(follower_log_id)
    return existing_follower_log


@router.get("/influencer/{influencer_id}", response_model=List[FollowerLog],  tags=["follower_logs"])
async def get_by_influencer_id_and_date_range(
    influencer_id: int,
    start_date: date,
    end_date: date
):
    follower_logs = await get_follower_logs_by_influencer_id_and_date_range(influencer_id, start_date, end_date)
    if not follower_logs:
        raise HTTPException(status_code=404, detail="No follower logs found for the given parameters")
    return follower_logs