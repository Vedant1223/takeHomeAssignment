import os
import groq
from dotenv import load_dotenv

load_dotenv()

# Initialize Groq client
client = groq.Client(api_key=os.getenv("GROQ_API_KEY"))

def generate_sql_from_nl(user_query):
    """
    Converts natural language query to SQL using Groq LLM
    Returns SQL query string or None if query is invalid
    """
    prompt = f"""
    You are an expert AI assistant whose only job is to generate safe, read-only SQL SELECT queries.
    Context:
    - You are working with a single PostgreSQL table named `venues`.
    - The table has the following columns:
      id (INTEGER), name (TEXT), location (TEXT), type (TEXT), price_range (TEXT), capacity (INTEGER), features (TEXT[]), available (BOOLEAN)
    Your task:
    - Convert natural language queries from users into **read-only** SQL **SELECT** statements.
    - Only generate queries that **filter/search** venues using WHERE clauses on the fields above.
    - NEVER generate any SQL that includes INSERT, UPDATE, DELETE, DROP, ALTER, CREATE, TRUNCATE, GRANT, or other modification statements.
    Security Rules:
    - If the user input is unrelated to venue search (e.g., jokes, instructions, irrelevant topics), or if it seems malicious (e.g., "delete all venues", "drop table"), then respond with:
      
      `null`
    - Your response **must contain only the SQL SELECT query** as plain text (no explanation, no markdown). Or return `null` if invalid.
    User input:
    \"\"\"{user_query}\"\"\"
    Respond with the SQL query or `null`.
    """
    
    try:
        # Call Groq API with the prompt
        response = client.chat.completions.create(
            model="llama3-8b-8192",  # Use appropriate model
            messages=[{"role": "user", "content": prompt}]
        )
        
        # Extract and parse response
        sql = response.choices[0].message.content.strip()
        
        # Check if the response is 'null' or contains invalid SQL operations
        if sql == 'null' or any(keyword in sql.upper() for keyword in [
            'INSERT', 'UPDATE', 'DELETE', 'DROP', 'ALTER', 'CREATE', 
            'TRUNCATE', 'GRANT'
        ]):
            return None
        
        return sql
    
    except Exception as e:
        print(f"Error generating SQL: {e}")
        return None

