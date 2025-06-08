# Tech Context: Shatably AI

## Technology Stack

### Backend
- **Python 3.8+**: Core programming language
- **FastAPI**: High-performance web framework for building APIs
- **Uvicorn**: ASGI server for running the FastAPI application

### AI Services
- **Gemini 2.0 Flash**: Primary LLM for chat functionality
- **Nebius API (black-forest-labs/flux-schnell)**: AI model for image generation

### Development Tools
- **Python virtual environment**: For dependency isolation
- **pip**: Package management
- **Git**: Version control

## Dependencies
Major dependencies listed in `requirements.txt`:
- fastapi: Web framework for API endpoints
- uvicorn: ASGI server for running FastAPI
- python-dotenv: Environment variable management
- python-multipart: Handling file uploads
- httpx: Asynchronous HTTP client for direct API calls to Nebius
- pydantic: Data validation and request/response models
- json: Processing API responses
- typing: Type annotations for better code structure

## Configuration Management
- Environment variables managed through `.env` file
- Configuration categories:
  - LLM Provider API Keys
  - LLM Configuration (temperature, tokens, etc.)
  - Chat Configuration
  - Image Generation Configuration
  - API Configuration

## API Endpoints
- **Chat**: `POST /chat/`
- **Image Generation**: `POST /image/generate`
- **Root**: `GET /`

## Development Environment
- Setup script (`setup.bat`) for Windows environment
- Manual setup instructions for other platforms
- Environment configured through `.env` file

## Technical Constraints
- API key requirements for external services (Nebius, Gemini)
- Rate limits from third-party AI services
- Stateful chat requiring history management
- Image size and quality limitations from Nebius API

## Integration Points
- **Gemini API**: For natural language processing using Gemini client
- **Nebius API**: For image generation using direct HTTP requests
  - Uses modular approach with separate request preparation and response processing
  - Implements comprehensive error handling
  - Returns base64-encoded images
- **Client Applications**: Through REST API endpoints with consistent response formats

## Deployment Considerations
- Currently runs locally on `http://localhost:8000`
- CORS configuration allows for cross-origin requests
- Environment variables must be properly configured in production
