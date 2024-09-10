from datetime import time
from fastapi import FastAPI, Request
from fastapi.security import HTTPBearer
from config.db import db_config
from config.database import database

from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse
from cruds.Auth import verify_token
from fastapi.security import HTTPBearer

from fastapi.middleware.cors import CORSMiddleware


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
from routers import FileUpload
from routers import InfluencerRating
from routers import InfluencerSocialAccount
from routers import Auth

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
app.include_router(FileUpload.router)
app.include_router(InfluencerRating.router)
app.include_router(InfluencerSocialAccount.router)
app.include_router(Auth.router)

origins = [
    "http://localhost:5173",
    "*"
]


app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"], # allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def root():
    return {
        "message": "Hello World"
        }
    
    


# Create a Bearer scheme instance
security = HTTPBearer()
@app.middleware("http")
async def check_token_middleware(request: Request, call_next):
    # Get the Authorization header
    authorization: str = request.headers.get("Authorization")

    # If no authorization header is found, raise an exception
    if authorization is None:
        return JSONResponse(status_code=401, content={"detail": "Authorization header missing"})

    # Split the "Bearer" token from the header
    token = authorization.split(" ")[1] if " " in authorization else None

    if token is None:
        return JSONResponse(status_code=401, content={"detail": "Invalid Authorization header format"})

    try:
        # Verify the token
        payload = verify_token(token)
        print(f"Token is valid, payload: {payload}")
        
        # You can add the payload (e.g., user info) to the request state if needed
        request.state.user = payload

    except Exception as e:
        print(f"Token verification failed: {str(e)}")
        return JSONResponse(status_code=401, content={"detail": str(e)})

    # Continue processing the request if the token is valid
    response = await call_next(request)

    return response
