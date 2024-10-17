import openai
import os
import json
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set your OpenAI API key from environment variable
openai.api_key = os.getenv("API_KEY")

def get_health_info(condition: str) -> str:
    """
    Fetch health-related information about a given medical condition and return JSON response.
    """
    prompt = f"""
    Provide detailed health information about '{condition}' including:
    - Common symptoms
    - Treatment options (non-surgical and surgical)
    - Average recovery time
    - Recommended treatment plans
    - Potential complications
    """
    
    try:
        response = openai.chat.completions.create(
            model="gpt-4o-mini", # Ensure you're using the correct model name
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=500,           # Set token limit
            temperature=0.3           # Lower temperature for factual responses
        )
        
        # Extract the response text
        result = response.choices[0].message['content'].strip()
        
        # Return the response as JSON
        return json.dumps({"info": result}, indent=2)
    
    except Exception as e:
        # Log the actual exception
        print(f"Error: {str(e)}")
        raise Exception(f"Error fetching health information: {str(e)}")
