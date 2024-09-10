import hashlib
import jwt
from fastapi import HTTPException
from datetime import datetime, timedelta
from models.User import User
from config.database import database  # Assume you have a database connection set up
from typing import Optional

SECRET_KEY = "kolab2024"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20

# Verify token
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        raise jwt.ExpiredSignatureError("Token has expired")
    except jwt.InvalidTokenError:
        raise jwt.InvalidTokenError("Invalid token")

def get_password_hash(password: str):
    """Hash the password using MD5"""
    return hashlib.md5(password.encode()).hexdigest()


async def authenticate_user(username: str, password: str) -> Optional[User]:
    """Authenticate the user with username and password"""
    query = "SELECT * FROM user WHERE username = :username"
    user = await database.fetch_one(query=query, values={"username": username})
    
    if not user:
        return None
    
    print(user["password"])
    print(password)
    if user["password"] == password:
        return User(**user)
    
    return None


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None):
    """Create JWT token"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


async def get_user_by_id(user_id: int) -> Optional[User]:
    """Get user by ID"""
    query = "SELECT * FROM user WHERE id = :id"
    user = await database.fetch_one(query=query, values={"id": user_id})
    if user:
        return User(**user)
    return None




async def reset_password(username: str, new_password: str):
    """Reset the user's password"""
  #  hashed_password = hashlib.md5(new_password.encode()).hexdigest()

    # Check if the user exists
    query = "SELECT * FROM user WHERE username = :username"
    user = await database.fetch_one(query=query, values={"username": username})

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Update the password
    update_query = """
        UPDATE user 
        SET password = :password, last_modified_date = NOW() 
        WHERE username = :username
    """
    await database.execute(query=update_query, values={"password": new_password, "username": username})

    return {"message": "Password updated successfully"}