# Venue Finder - AI-Powered Venue Search Application

A full-stack application that converts natural language queries into SQL and provides venue recommendations based on user criteria.

## Project Overview

Venue Finder uses a FastAPI backend with LLM-powered natural language processing to convert user queries into SQL. The Angular frontend provides an intuitive interface for searching venues and viewing the results.

### Key Features

- **Natural Language Search**: Enter queries in plain English (e.g., "Find all bars in downtown")
- **AI-Powered**: Converts natural language to SQL using LLM technology (Groq)
- **SQL Transparency**: View the SQL query generated from your natural language input
- **Modern UI**: Responsive design with intuitive venue cards display

## Technology Stack

### Backend
- **FastAPI**: High-performance Python web framework
- **SQLAlchemy**: SQL toolkit and ORM
- **Groq**: LLM API for natural language processing
- **PostgreSQL**: Database for venue storage

### Frontend
- **Angular**: Standalone component architecture
- **TypeScript**: Type-safe JavaScript
- **HTML/CSS**: Modern, responsive design

## Project Structure

```
venue-finder/
│
├── frontend/               # Angular application
│   ├── src/
│   │   ├── app/
│   │   │   ├── components/ # Standalone components
│   │   │   ├── services/   # API services
│   │   │   └── ...
│   │   └── ...
│   └── ...
│
├── backend/
│   ├── venv/               # Python virtual environment
│   ├── main.py             # FastAPI application
│   ├── llm_agent.py        # LLM integration for NL to SQL
│   ├── requirements.txt    # Python dependencies
│   ├── venues.json         # Sample venue data
│   └── .env                # Environment variables
│
└── README.md               # This file
```

## Setup Instructions

### Backend Setup

1. Navigate to the backend directory:
   ```bash
   cd backend
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file with the following variables:
   ```
   DATABASE_URL=postgresql://username:password@localhost:5432/venue_db
   GROQ_API_KEY=your_groq_api_key
   ```

5. Start the FastAPI server:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```bash
   cd frontend
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

3. Start the Angular development server:
   ```bash
   ng serve
   ```

4. Open your browser and navigate to `http://localhost:4200`

## API Endpoints

### Venue API

- `GET /venue/{venue_id}`: Get a specific venue by ID
- `POST /query`: Convert natural language to SQL
- `POST /recommend`: Get venue recommendations based on natural language query

## Using the Application

1. Enter a natural language query in the search box (e.g., "Find all bars in downtown with capacity over 100")
2. Click "Search Venues" to see matching venues
3. Click "Show SQL" to see the SQL query generated from your natural language input

## Example Queries

- "Show me all bars in downtown"
- "Find venues with capacity over 200 that are available"
- "List all restaurants with outdoor seating"
- "Show venues that are bars or clubs in the high price range"

## Database Schema

The application uses a PostgreSQL database with a single `venues` table:

```
venues
├── id (INTEGER)
├── name (TEXT)
├── location (TEXT)
├── type (TEXT)
├── price_range (TEXT)
├── capacity (INTEGER)
├── features (TEXT[])
└── available (BOOLEAN)
```

## Security Considerations

- The application uses an LLM to generate SQL queries but implements strict validation to ensure only SELECT statements can be executed
- CORS is configured to allow only specified origins

## Future Enhancements

- User authentication and saved searches
- Advanced filtering and sorting options
- Map view for venue locations
- Venue ratings and reviews
- Mobile application
