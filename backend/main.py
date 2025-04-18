from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
from pydantic import BaseModel
# from llm_agent import generate_sql_from_nl

class QueryInput(BaseModel):
    query: str

load_dotenv()

app = FastAPI()

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

@app.get("/")
def root():
    return {"message": "FastAPI + PostgreSQL is working 🚀"}



@app.get("/venue/{venue_id}")
def get_venue_by_id(venue_id: int):
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM venues WHERE id = :id"), {"id": venue_id})
            row = result.fetchone()

            if row is None:
                raise HTTPException(status_code=404, detail="Venue not found")

            # Convert SQLAlchemy Row to dict
            venue = dict(row._mapping)

        return {"status": "success", "venue": venue}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

