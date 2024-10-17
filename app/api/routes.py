from fastapi import APIRouter, HTTPException
from app.services.gpt_service import get_gpt_response, get_health_info
from app.models.gpt_model import GPTRequest, GPTResponse
from pydantic import BaseModel





router = APIRouter()

@router.post("/gpt/", response_model=GPTResponse)
async def chat_gpt(request: GPTRequest):
    try:
        # Call the GPT service with the additional parameters
        response = await get_gpt_response(
            request.prompt,
            request.max_tokens,
            request.temperature,  # Pass temperature
            request.top_p         # Pass top_p
        )
        
        if not response:
            raise HTTPException(status_code=501, detail="No response from GPT")

        return GPTResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=501, detail=f"Error: {str(e)}")


# Define request model for health information
class HealthInfoResponse(BaseModel):
    info: str

# GET /health-info/ route for medical information using query parameters
@router.get("/health-info/", response_model=HealthInfoResponse)
async def get_health_info_route(condition: str):
    
    try:
        # Call the get_health_info function with the condition from query parameters
        info = get_health_info(condition)
        
        if not info:
            raise HTTPException(status_code=404, detail="No information found for the condition")

        return HealthInfoResponse(info=info)
    
    except Exception as e:
        # Log the exception details and raise an HTTPException
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching health information: {str(e)}")
        
    
    except Exception as e:
        # Log the exception details and raise an HTTPException
        print(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=f"Error fetching health information: {str(e)}")

    


    
    
   
    



