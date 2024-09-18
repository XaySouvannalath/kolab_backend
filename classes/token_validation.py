import os
import jwt
from fastapi import HTTPException

# Retrieve the secret key and algorithm from environment variables
SECRET_KEY ="KOLAB2024"
ALGORITHM = os.getenv('ALGORITHM')

# Function to verify the access token extracted from the request
def verify_access_token(request):
    # Extract the token from the request
    token = get_token_from_request(request)
    
    try:
        # Decode and verify the token using the secret key and algorithm
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        # Raise an HTTPException with status code 401 if the token has expired
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        # Raise an HTTPException with status code 401 if the token is invalid
        raise HTTPException(status_code=401, detail="Invalid token")