from pydantic import BaseModel

class GPTRequest(BaseModel):
    prompt: str
    max_tokens: int = 300
    temperature: float = 0.7  # Add temperature for response randomness
    top_p: float = 1.0        # Add top_p for controlling diversity

class GPTResponse(BaseModel):
    response: str
