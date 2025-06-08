# Revised Shatably AI Implementation Plan

## Overview

Based on your requirements, I've revised the implementation plan to include a services file that will handle the endpoints logic and call the appropriate functions from the chat and photo modules. The plan also includes moving environment variables to the .env file.

## Revised File Structure

```
/Shatably_AI/
├── main.py                 # Application entry point with FastAPI setup
├── .env                    # Environment variables
├── requirements.txt        # Project dependencies
├── services.py             # API endpoints that call functions from chat/photo modules
├── chat.py                 # Chat functionality with Gemini integration
├── photo.py                # Image generation functionality
└── utils.py                # Utility functions for history management
```

## Environment Variables to Move to .env

From analyzing the existing code, these variables should be moved to .env:

```
# From photo.py
NEBIUS_API_KEY=eyJhbGciOiJIUzI1NiIsImtpZCI6IlV6SXJWd1h0dnprLVRvdzlLZWstc0M1akptWXBvX1VaVkxUZlpnMDRlOFUiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiJnb29nbGUtb2F1dGgyfDExNTE3NDA1MzEwNDkyNDE1MTI2NSIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIiwiaXNzIjoiYXBpX2tleV9pc3N1ZXIiLCJhdWQiOlsiaHR0cHM6Ly9uZWJpdXMtaW5mZXJlbmNlLmV1LmF1dGgwLmNvbS9hcGkvdjIvIl0sImV4cCI6MTkwNDk4OTk0NCwidXVpZCI6ImE5YTIwNjlhLTM3ODktNDc3OC1iZGQ3LTg3MWVjMDA5YjRjOCIsIm5hbWUiOiJzYWh0YWJseSIsImV4cGlyZXNfYXQiOiIyMDMwLTA1LTE0VDExOjUyOjI0KzAwMDAifQ.v2v7T9Fdtwe2VSbD8YqYJ6N7gd5vR1nz3YWIQU26uV8
NEBIUS_BASE_URL=https://api.studio.nebius.com/v1/
IMAGE_MODEL=black-forest-labs/flux-schnell
IMAGE_WIDTH=520
IMAGE_HEIGHT=520
IMAGE_STEPS=16

# From chat.py
GEMINI_API_KEY=AIzaSyAjzM_BmIXGqMVVSGb1Lcu9-kMNO_1FmN8
TEMPERATURE=1
TOP_K=3
TOP_P=0.85
MAX_OUTPUT_TOKENS=1024
CHAT_MODEL=gemini-2.0-flash
HISTORY_FILE=chat_history.json

# General settings
CORS_ORIGINS=["*"]
```

## Implementation Steps

### 1. Environment Setup

- Create `.env` file with all identified environment variables
- Update `requirements.txt` with required dependencies

### 2. Refactor Existing Code

- Refactor `photo.py` to be a module with functions instead of a standalone app
  - Move API key to .env
  - Convert the generate_image endpoint to a function that can be called from services.py

- Refactor `chat.py` to be a module with functions instead of a standalone app
  - Move API key and configuration to .env
  - Convert the chat endpoint to a function that can be called from services.py

### 3. Create Services Module (services.py)

- Implement API endpoints that call functions from chat.py and photo.py
- Handle request validation and error handling
- Ensure proper routing of requests to the appropriate service functions

### 4. Utility Functions (utils.py)

- Implement chat history management functions
- Add helper functions for file operations
- Create functions to load environment variables

### 5. Main Application (main.py)

- Set up FastAPI application
- Configure CORS middleware
- Import and include routes from services.py

### 6. Testing

- Test chat functionality
- Test image generation functionality
- Verify proper error handling

## Detailed Module Responsibilities

### main.py
- Initialize FastAPI application
- Configure middleware
- Import routes from services.py
- Run the application

### services.py
- Define API endpoints
- Validate incoming requests
- Call appropriate functions from chat.py or photo.py
- Handle responses and errors

### chat.py
- Implement Gemini API integration
- Provide functions for chat processing
- Handle chat history management

### photo.py
- Implement Nebius/OpenAI API integration
- Provide functions for image generation

### utils.py
- Implement utility functions
- Manage file operations
- Handle environment variable loading

## Timeline

| Task | Estimated Time |
|------|----------------|
| Environment Setup | 1 hour |
| Refactor Existing Code | 3 hours |
| Create Services Module | 2 hours |
| Utility Functions | 2 hours |
| Main Application | 1 hour |
| Testing | 2 hours |
| **Total** | **11 hours** |

## Next Steps After Approval

Once this implementation plan is approved, we will proceed with the following steps:

1. Create the `.env` file with all identified environment variables
2. Refactor the existing code in photo.py and chat.py
3. Implement the services.py module
4. Create utils.py for utility functions
5. Develop main.py as the application entry point
6. Test the complete application