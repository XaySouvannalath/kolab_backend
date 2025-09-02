from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from datetime import timedelta
from cruds.Auth import *
from typing import Union
from fastapi.responses import JSONResponse

from cruds.RoleMenu import get_role_menu_by_role_id
from models.Auth import LoginModel
from models.RoleMenu import RoleMenu
from models.User import PasswordReset
import json

router = APIRouter(
    tags=["Auth"]
)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/login")

@router.post("/login")
async def login(form_data: LoginModel):
    user = await authenticate_user(form_data.username, form_data.password)
    if not user:
        # raise HTTPException(
        #     status_code=status.HTTP_401_UNAUTHORIZED,
        #     detail="Incorrect username or password",
        #     headers={"WWW-Authenticate": "Bearer"},
        # )
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={
                "success": False,
                "message": "Incorrect username or password",
                
            }
        )
    
    access_token_expires = timedelta(weeks=1)  # Token will expire in 1 week
    access_token = create_access_token(
        data={"sub": user.username, "id": user.id}, expires_delta=access_token_expires
    )
    menus = await get_role_menu_by_role_id(user.user_role_id)
    menu_json = []
    menu_model = []
    for menu in menus:
        menu_model =  RoleMenu(
            id = menu["id"],
            role_id = menu["role_id"],
            menu_id = menu["menu_id"],
            menu = menu["menu"],
            route = menu["route"]
        )
        menu_json.append(menu_model)

    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "success": True,
            "access_token": access_token, 
            "token_type": "bearer",
            "first_name": user.first_name,
            "last_name": user.last_name,
            "menu": [m.__dict__ for m in menu_json],
            "role_id": user.user_role_id
             
        })


@router.get("/logout")
async def logout(token: str = Depends(oauth2_scheme)):
    # For stateless JWT, there's no real logout. 
    # You would manage it with token blacklisting in a real-world scenario.
    return {"message": "Successfully logged out"}


@router.get("/me")
async def get_me(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("id")
        if user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication")
        user = await get_user_by_id(user_id)
        if user is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid authentication")
    except jwt.PyJWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials")
    
    return user


@router.post("/reset-password")
async def reset_password_api(data: PasswordReset):
    """API to reset the user's password"""
    return await reset_password(data.username, data.new_password)
