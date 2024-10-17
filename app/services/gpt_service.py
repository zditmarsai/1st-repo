# app/services/gpt_service.py
import openai
from app.config import settings
import os
from dotenv import load_dotenv

(load_dotenv)

# Set your OpenAI API key
openai.api_key = os.getenv("API_KEY")


# Update the service to accept temperature and top_p
async def get_gpt_response(prompt: str, max_tokens: int, temperature: float = 0.7, top_p: float = 1.0) -> str:
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            max_tokens=max_tokens,
            temperature=temperature,  # Use temperature to control randomness
            top_p=top_p,               # Use top_p to control response diversity
            
        )
        return response.choices[0]
    except Exception as e:
        return f"Error: {str(e)}"
    
def get_health_info(condition: str):
    prompt = f"""
    Provide detailed health information about '{condition}' including:
    - Common symptoms
    - Treatment options (non-surgical and surgical)
    - Average recovery time
    - Recommended treatment plans
    - Potential complications
    """
    response = openai.chat.completions.create(
        messages=[
                {"role": "system", "content": "You are a helpful medical assistant."},
                {"role": "user", "content": prompt}
                    ],
        model="gpt-4o-mini",
        max_tokens=500,
        temperature=0.3,  # Lower temperature for more factual answers
       
    )
    return response.choices[0].message.content.strip()
    



