# AutoTriage Server

A FastAPI application used to triage incoming emails.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Create a virtual environment**:
   ```bash
   python -m venv .venv
   ```

2. **Activate the virtual environment**:
   
   On macOS/Linux:
   ```bash
   source .venv/bin/activate
   ```
   
   On Windows:
   ```bash
   .venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

### Running the Server

#### Development Mode

Run the server with auto-reload enabled for development:

```bash
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Production Mode

For production, run without the `--reload` flag:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

The server will be available at:
- **Local**: http://localhost:8000
- **Network**: http://0.0.0.0:8000

### API Documentation

Once the server is running, you can access:

- **Interactive API docs (Swagger UI)**: http://localhost:8000/docs
- **Alternative API docs (ReDoc)**: http://localhost:8000/redoc
- **OpenAPI JSON**: http://localhost:8000/openapi.json

### Available Endpoints

- `GET /` - Root endpoint with welcome message
- `GET /health` - Health check endpoint

### Running Tests

Run the test suite using pytest:

```bash
pytest
```

For verbose output:
```bash
pytest -v
```

For coverage report:
```bash
pytest --cov=app
```

### Configuration

The application uses Pydantic Settings for configuration management. You can configure the application using:

1. **Default values in `app/core/config.py`**

Key configuration options:
- `PROJECT_NAME`: Application name
- `VERSION`: Application version
- `DEBUG`: Enable debug mode
- `HOST`: Server host
- `PORT`: Server port
- `ALLOWED_HOSTS`: CORS allowed hosts