# System Patterns: Shatably AI

## Architecture Overview
Shatably AI follows a modular architecture with clear separation of concerns:

```
API Layer (FastAPI) → Service Layer → Model Integration
```

## Key Components

### API Layer
- Built with FastAPI for high-performance, asynchronous API endpoints
- Handles HTTP requests and responses
- Manages API authentication and validation
- Defined in `main.py` and `services.py`

### Chat Module
- Manages conversation state and history
- Integrates with LLM providers (primarily Gemini)
- Handles system instructions and conversation context
- Implements in `chat.py`

### Image Generation Module
- Processes image generation requests with modular design:
  - `prepare_image_request`: Builds API URL, headers, and payload
  - `process_image_response`: Extracts and validates image data
  - `generate_image`: Orchestrates the API request flow
- Uses direct HTTP requests via httpx to Nebius API
- Implements comprehensive error handling at multiple levels
- Returns base64-encoded images for frontend consumption
- Implemented in `photo.py`

### Utilities
- Configuration management via environment variables
- Helper functions for API interactions
- Common utilities shared across modules
- Implemented in `utils.py`

## Design Patterns

### Dependency Injection
- Environment variables configure system behavior
- Models and services are configured through environment settings

### Service-Oriented Architecture
- Clear separation between API endpoints and business logic
- Modular components with specific responsibilities

### Stateful Chat
- Maintains conversation history for context awareness
- Stores chat history in JSON format

## Data Flow

### Chat Flow
1. User sends message (text and/or image) to `/chat/` endpoint
2. `services.py` processes request and calls chat service
3. `chat.py` formats prompt with system instructions and history
4. LLM (Gemini) generates response
5. Response is returned to user and chat history is updated

### Image Generation Flow
1. User sends prompt to `/image/generate` endpoint
2. `services.py` processes request and calls image generation service
3. `photo.py` prepares the request (URL, headers, payload)
4. Direct HTTP request is made to Nebius API using httpx
5. Response is validated and processed to extract base64 image
6. Generated image is returned to user with appropriate format

## Error Handling
- Multi-layered error handling strategy throughout the system
- Specific error types with appropriate HTTP status codes (400, 500, etc.)
- Detailed error messages for troubleshooting
- Input validation before API calls to prevent invalid requests
- Response validation to handle unexpected API responses
- Network error handling for API connectivity issues
- Graceful degradation when services are unavailable
