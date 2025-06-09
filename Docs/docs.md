# Shatably AI Documentation

## Table of Contents
1. [Project Overview](#project-overview)
2. [Setup Instructions](#setup-instructions)
3. [API Documentation](#api-documentation)
4. [Technical Details](#technical-details)
5. [Deployment Guide](#deployment-guide)
6. [Development Guide](#development-guide)

## Project Overview

Shatably AI is an advanced interior design assistant that combines multiple AI capabilities to provide design consultation, image generation, and image editing services. The system uses Google's Gemini AI for chat and image analysis, and DALL-E for image generation.

### Key Features
- AI-powered interior design consultation
- Image generation for interior designs
- Image editing and modification
- Multi-modal interaction (text + images)

## Setup Instructions

### Prerequisites
- Python 3.9 or higher
- pip package manager
- Git

### Environment Setup
1. Clone the repository:
```bash
git clone https://github.com/yourusername/Shatably_AI.git
cd Shatably_AI
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables:
Create a `.env` file with:
```env
GEMINI_API_KEY=your_gemini_api_key
OPENAI_API_KEY=your_openai_api_key
```

### Quick Start
Run the setup script:
```bash
setup.bat  # On Windows
./setup.sh  # On Unix/Linux
```

## API Documentation

### Chat Endpoint
```python
POST /chat/
```
Parameters:
- `message` (string, required): User's message
- `image` (file, optional): Image file to analyze
- `user_id` (string, optional): User identifier

Response:
```json
{
    "response": "AI generated response",
    "success": true
}
```

### Image Generation Endpoint
```python
POST /image/generate
```
Parameters:
- `prompt` (string, required): Description of desired image

Response:
```json
{
    "success": true,
    "image": "base64_encoded_image",
    "message": "Generation details"
}
```

### Image Editing Endpoint
```python
POST /edit/
```
Parameters:
- `prompt` (string, required): Editing instructions
- `image` (file, required): Image to edit

Response:
```json
{
    "success": true,
    "edited_image": "base64_encoded_image",
    "message": "Edit details"
}
```

## Technical Details

### Core Components

#### 1. main.py
- FastAPI application configuration
- Router integration
- CORS middleware setup
- Error handling

#### 2. services.py
- API endpoint implementations
- Request/response models
- Error handling middleware
- Router definitions

#### 3. chat.py
- Gemini AI integration
- Chat processing logic
- Multi-modal input handling
- Conversation context management

#### 4. photo.py
- DALL-E integration
- Image generation logic
- Image format handling
- Response formatting

#### 5. edit_photo.py
- Gemini Vision AI integration
- Image editing capabilities
- Image transformation logic

#### 6. utils.py
- Helper functions
- Common utilities
- Configuration management
- Error handling utilities

### Models Used

1. **Google Gemini AI**
   - Model: gemini-2.0-flash-exp
   - Features: Multi-modal processing
   - Use cases: Chat, image analysis

2. **DALL-E**
   - Version: Latest
   - Features: Image generation
   - Use cases: Interior design visualization

## Deployment Guide

### Railway Deployment

1. **Configuration**
   - Set environment variables in Railway dashboard
   - Configure deployment settings
   - Set up health checks

2. **Deployment Process**
   - Automatic deployment on push to main branch
   - Docker container deployment
   - Environment variable injection

### Local Deployment

1. **Development Server**
```bash
uvicorn main:app --reload
```

2. **Production Server**
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## Development Guide

### Project Structure
```
Shatably_AI/
├── main.py
├── services.py
├── chat.py
├── photo.py
├── edit_photo.py
├── utils.py
├── requirements.txt
├── .env
├── .gitignore
├── setup.bat
├── Docs/
│   └── docs.md
└── systemdesign.md
```

### Best Practices
1. **Code Organization**
   - Modular design
   - Clear separation of concerns
   - Consistent error handling

2. **API Design**
   - RESTful principles
   - Clear documentation
   - Proper validation

3. **Security**
   - Environment variable usage
   - API key protection
   - Input validation

4. **Testing**
   - Unit tests
   - Integration tests
   - API endpoint tests

### Git Workflow
1. Feature branches
2. Pull request reviews
3. Version tagging
4. Changelog maintenance

## Error Handling

### Common Error Codes
- 400: Bad Request
- 401: Unauthorized
- 403: Forbidden
- 404: Not Found
- 500: Internal Server Error

### Error Response Format
```json
{
    "error": "Error description",
    "status_code": 400,
    "details": "Additional information"
}
```

## Maintenance

### Regular Tasks
1. Update dependencies
2. Monitor API usage
3. Review logs
4. Update documentation

### Troubleshooting
1. Check logs
2. Verify API keys
3. Test endpoints
4. Review configurations 