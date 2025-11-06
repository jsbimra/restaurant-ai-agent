from fastapi import FastAPI, Request, HTTPException
from main_agent import agent
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

@app.get("/find-restaurants")
async def find_restaurants(q: str, lat: float, lng: float, request: Request):
    key = request.headers.get("x-api-key")
    if key != os.getenv("FRONTEND_SECRET_KEY"):
        raise HTTPException(status_code=403, detail="Unauthorized")

    response = agent.run(f"{q}. Use latitude {lat} and longitude {lng}")
    return {"response": response}
