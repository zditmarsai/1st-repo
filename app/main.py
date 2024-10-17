from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from starlette.exceptions import HTTPException as StarletteHTTPException
from app.api import routes
import json

app = FastAPI()

# Include API routes from the app/api/routes.py
app.include_router(routes.router)

# Mount the static directory to serve static files
app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve index.html at the root
@app.get("/", response_class=HTMLResponse)
async def read_index():
    with open("static/index.html") as f:
        return f.read()

@app.get("/health-info/", response_class=JSONResponse)
async def get_health_info(condition: str):
    try:
        # Dynamically return information based on the condition
        info = f"Details about the condition: {condition}"
        return {"info": info}
    
    except Exception as e:
        return JSONResponse(status_code=500, content={"message": str(e)})



# Custom 404 error handler
@app.exception_handler(StarletteHTTPException)
async def custom_404_handler(request: Request, exc: StarletteHTTPException):
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={"message": "Oops! The resource you are looking for does not exist."},
        )
    return JSONResponse(
        status_code=exc.status_code,
        content={"message": exc.detail},
    )

