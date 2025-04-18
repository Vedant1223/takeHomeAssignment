from fastapi import FastAPI
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

from pydantic import BaseModel
from llm_agent import generate_sql_from_nl

class QueryInput(BaseModel):
    query: str

# Load .env
load_dotenv()

# Initialize FastAPI
app = FastAPI()

# Get DB URL from .env
DATABASE_URL = os.getenv("DATABASE_URL")

# Connect to PostgreSQL using SQLAlchemy
engine = create_engine(DATABASE_URL)

@app.get("/")
def root():
    return {"message": "FastAPI + PostgreSQL is working 🚀"}

# Optional test route to check DB connection
@app.get("/db-test")
def test_db():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT NOW()"))
            current_time = result.scalar()
        return {"status": "success", "timestamp": current_time}
    except Exception as e:
        return {"status": "error", "message": str(e)}

