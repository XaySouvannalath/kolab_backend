from datetime import time
from fastapi import FastAPI, Request, Response, status
from fastapi.security import HTTPBearer
from config.db import db_config
from config.database import database

from fastapi import Request, HTTPException
from fastapi.responses import JSONResponse

from cruds.Auth import verify_token
from fastapi.security import HTTPBearer

from fastapi.middleware.cors import CORSMiddleware 

# from starlette.middleware.cors import CORSMiddleware


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
    "http://localhost:5173"
]



# app.add_middleware(
#     CORSMiddleware,
    
    
#     # allow_origins=origins,
#     allow_origins=["*"], # allow all origins
#     allow_credentials=True,
#     allow_methods=["*"],
#     allow_headers=["*", "Authorization"],
    
# )
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
# security = HTTPBearer()
@app.middleware("http")
async def check_token_middleware(request: Request, call_next):
    # print("calling api")
    # Get the Authorization header
    # print(request.headers)
    authorization = request.headers.get("Authorization")
    test = request.headers.get("saiyavong")
    # print(authorization)
    # print(test)
    response = await call_next(request)
    # return response

    req_path = request.url.path
    if req_path == '/login' or req_path == '/docs' or req_path == '/openapi.json' or req_path == '/files':
         return response
        #  return response
    else:
        # If no authorization header is found, raise an exception
        if authorization is None:
            return JSONResponse(status_code=401, content={
                "success": False,
                "detail": "Authorization header missing"})
        else:
            token = authorization.split(" ")[1] if " " in authorization else None
            # print(token)
            # return response
            if token is None:
                return JSONResponse(status_code=401, content={
                    "detail": "Invalid Authorization header format"})
            else:
                try:
                #     # Verify the token
                    payload = verify_token(token)
                    # You can add the payload (e.g., user info) to the request state if needed
                    # print("Payload")
                    # print(payload)
                    request.state.user = payload
                   
                    # return response
                    if payload == False:
                        return JSONResponse(status_code=401, content={"success": False,"message": "Token has expired"})
                    else:
                      
                        return response
                except Exception as e:
                    print(f"Token verification failed: {str(e)}")
                    return JSONResponse(status_code=401, content={"success": False,"message": "Token has expired"})

    

 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,  # Optional: Allow cookies and authentication headers
    allow_methods=["*"],  # Allow all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],  # Allow all headers
)