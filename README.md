# Katalon Assistant with MCP Integration

An AI-powered assistant for Katalon documentation that leverages Google's Gemini model through LangChain and provides an interactive interface with Chainlit.

## Features

- Query Katalon documentation through a conversational interface
- Stream responses for a natural chat experience
- Integrate with MCP (Model Control Protocol) servers for external tools
- FastAPI backend with Chainlit frontend

## Prerequisites

- Python 3.11 or higher
- Poetry (recommended) or pip

## Setup and Installation

### Using Poetry (Recommended)

#### Windows

1. Clone this repository:
   ```
   git clone https://github.com/username/katalon-assistant.git
   cd katalon-assistant
   ```

2. Install Poetry if not already installed:
   ```
   (Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
   ```

3. Create and activate a virtual environment:
   ```
   python -m venv venv
   .\venv\Scripts\activate
   ```

4. Install dependencies:
   ```
   poetry install
   ```

5. Set up environment variables:
   - Create a `.env` file in the root directory with:
     ```
     GOOGLE_API_KEY=your_google_api_key
     ```
   - Or set environment variables in PowerShell:
     ```
     $env:GOOGLE_API_KEY="your_google_api_key"
     ```

#### macOS

1. Clone this repository:
   ```
   git clone https://github.com/username/katalon-assistant.git
   cd katalon-assistant
   ```

2. Install Poetry if not already installed:
   ```
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. Create and activate a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

4. Install dependencies:
   ```
   poetry install
   ```

5. Set up environment variables:
   - Create a `.env` file in the root directory with:
     ```
     GOOGLE_API_KEY=your_google_api_key
     ```
   - Or set environment variables in terminal:
     ```
     export GOOGLE_API_KEY="your_google_api_key"
     ```

## Running the Application

### 1.  Activate Virtual Environment

- #### Windows

```
python -m venv venv
.\venv\Scripts\activate
```

- #### MacOs

```
python3 -m venv venv
source venv/bin/activate
```

### 2.  Using Poetry

```
fastapi dev main.py
```

The application will be available at ```http://localhost:8000```

The api documentation will be available at ```http://localhost:8000/docs```

## Architecture

- `main.py`: FastAPI application entry point
- `cl_app.py`: Chainlit application
- `app/api/ai_agent_routes.py`: API routes for the AI agent
- `app/llm/ai_agent.py`: LLM integration with Gemini
- `app/embeddings/embeddings.py`: Text embedding functionality
- `chainlit.md`: MCP server configuration and welcome message

## Development

To modify the application:

1. Edit the API routes in `app/api/ai_agent_routes.py`
2. Update the LLM functionality in `app/llm/ai_agent.py`
3. Modify the Chainlit interface in `cl_app.py`
