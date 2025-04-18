from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from llm_agent import generate_sql_from_nl

class QueryInput(BaseModel):
    query: str

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],  # Angular default port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


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
    

@app.post("/query")
def showQuery(input: QueryInput):
    sql_query = generate_sql_from_nl(input.query)
    if not sql_query:
            return {
                "status": "error",
                "message": "Could not understand your request or it appears to be invalid. Please try rephrasing."
            }

    return {
            "status": "success",
            "sql_executed": sql_query
    }


@app.post("/recommend")
def recommend_venues(input: QueryInput):
    try:
        # Generate SQL from natural language
        sql_query = generate_sql_from_nl(input.query)
        
        if not sql_query:
            return {
                "status": "error",
                "message": "Could not understand your request or it appears to be invalid. Please try rephrasing."
            }
        
        # Execute the SQL query
        with engine.connect() as conn:
            result = conn.execute(text(sql_query))
            venues = [dict(row._mapping) for row in result.fetchall()]
        
        # Return the venues along with the query that was executed (for transparency)
        return {
            "status": "success",
            "venues": venues
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))