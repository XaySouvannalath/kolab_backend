from typing import List
from fastapi import APIRouter, HTTPException
from models.InfluencerRating import InfluencerRating
from cruds.InfluencerRating import *
router = APIRouter()



@router.get("/influencer-rating/{influencer_id}")
async def get_influencer_rating(influencer_id: int):
    results = await get_influencer_ratings(influencer_id=influencer_id)
    # if not results:
    #     raise HTTPException(status_code=404, detail="Ratings not found for this influencer")

        # Create a dictionary to group scores by influencer_id
    categories = []  # Extract categories (labels)
    series_data = {}  # Group by influencer_id

    for entry in results:
        category = entry["category"]
        influencer_id = entry["influencer_id"]
        score = entry["score"]

        # Add the category to the labels list if not already present
        if category not in categories:
            categories.append(category)

        # Group scores by influencer_id
        if influencer_id not in series_data:
            series_data[influencer_id] = {
                "name": f"Radar Series {influencer_id}",
                "data": []
            }
        
        series_data[influencer_id]["data"].append(score)

    # Convert series_data to a list for the final series format
    series = list(series_data.values())

    # Prepare the final output format
    options = {
        "series": series,
        "labels": categories
    }
    
    return options
