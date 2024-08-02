from fastapi import FastAPI
from config.db import db_config
from config.database import database

#import router
from routers import agency
from routers import utilities
from routers import influencer
from routers import AgencyInfluencer
from routers import ContentStyle
from routers import FollowerLog
from routers import ImageResource
from routers import InfluencerAddress
from routers import Power
from routers import InfluencerPower
from routers import InfluencerReview
from routers import Tag
from routers import InfluencerTag
from routers import Menu
from routers import Post
from routers import PriceOfPost
from routers import Province
from routers import ReviewImage
from routers import ReviewInsight
from routers import RoleMenu
from routers import SocialPlatform
from routers import User
from routers import UserRole


app = FastAPI()

app.include_router(agency.router)
app.include_router(utilities.router)
app.include_router(influencer.router)
app.include_router(AgencyInfluencer.router)
app.include_router(ContentStyle.router)
app.include_router(FollowerLog.router)
app.include_router(ImageResource.router)
app.include_router(InfluencerAddress.router)
app.include_router(Power.router)
app.include_router(InfluencerPower.router)
app.include_router(InfluencerReview.router)
app.include_router(Tag.router)
app.include_router(InfluencerTag.router)
app.include_router(Menu.router)
app.include_router(Post.router)
app.include_router(PriceOfPost.router)
app.include_router(Province.router)
app.include_router(ReviewImage.router)
app.include_router(ReviewInsight.router)
app.include_router(RoleMenu.router)
app.include_router(SocialPlatform.router)
app.include_router(User.router)
app.include_router(UserRole.router)

@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def root():
    return {
        "message": "Hello World",
        "dbname": db_config.some_global_value,
        "db_config": db_config
        }


