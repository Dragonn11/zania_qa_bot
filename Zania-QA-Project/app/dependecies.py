from fastapi import Header, HTTPException

async def validate_api_key(x_api_key: str = Header(...)):
    """
    Validates the API key provided in the request header.
    """
    expected_api_key = "your_expected_api_key_here"
    
    if x_api_key != expected_api_key:
        raise HTTPException(status_code=401, detail="Invalid API Key")
