
"""
# app/services/auth.py
from fastapi import Depends, HTTPException, Security
from fastapi.security.api_key import APIKeyHeader

# Define the expected API key (you could load this from an environment variable)
API_KEY = "moonsoapnote"
api_key_header = APIKeyHeader(name="X-API-Key")

# Define the function to validate the API key
async def get_api_key(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(
            status_code=403,
            detail="Could not validate API key, You do not have permission to access this API."
        )
"""