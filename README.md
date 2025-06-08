# Shatably AI

Shatably AI is an interior design assistant application that provides chat-based design advice and image generation capabilities.

## Features

- Chat with an AI interior design expert (MR Shatbly)
- Generate interior design images based on prompts
- Support for text and image inputs in chat

## Setup

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Installation

1. **Windows Setup**

   Run the setup script to create a virtual environment and install dependencies:

   ```
   setup.bat
   ```

2. **Manual Setup**

   If you prefer to set up manually or are using a different operating system:

   ```bash
   # Create a virtual environment
   python -m venv venv

   # Activate the virtual environment
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate

   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Environment Variables**

   Create a `.env` file in the root directory with the following variables:

   ```
   # LLM Provider API Keys
   NEBIUS_API_KEY=your_nebius_api_key
   GEMINI_API_KEY=your_gemini_api_key

   # LLM Configuration
   TEMPERATURE=1
   TOP_K=3
   TOP_P=0.85
   MAX_OUTPUT_TOKENS=1024

   # Chat Configuration
   CHAT_MODEL=gemini-2.0-flash
   CHAT_HISTORY_FILE=chat_history.json
   SYSTEM_INSTRUCTION=You are an expert interior designer chatbot working in an app called 'Shatbly'. You give friendly, personalized home design advice based on the user's room type, style, color, and preferences. Suggest ideas for layout, colors, furniture, and decor in a warm and helpful tone. Your name is MR Shatbly. Use a lot of fitting emojis in every message. Start, end, and decorate your sentences with emojis that match the mood and topic. Be expressive and visually engaging, reduce asking. When user ask you in arabic resonse arabic. If you are asked about anything unrelated to furniture or interior design, kindly reply that you are a 'Shatbly' assistant specialized in interior and furniture consultations, and that you're here anytime to help with anything related to home design.

   # Image Generation Configuration
   IMAGE_MODEL=nebius-image-v1.0
   IMAGE_WIDTH=1024
   IMAGE_HEIGHT=1024
   IMAGE_STEPS=50
   IMAGE_BASE_URL=https://api.nebius.cloud/foundation-models/v1/inference/nebius-image-v1.0

   # API Configuration
   CORS_ORIGINS=["*"]
   ```

## Running the Application

1. Activate the virtual environment (if not already activated):

   ```bash
   # On Windows
   venv\Scripts\activate
   # On macOS/Linux
   source venv/bin/activate
   ```

2. Start the application:

   ```bash
   python main.py
   ```

3. The API will be available at `http://localhost:8000`

## API Endpoints

- **Chat**: `POST /chat/`
  - Parameters:
    - `message`: Text message (required)
    - `image`: Image file (optional)
    - `user_id`: User identifier (optional, defaults to "default")

- **Image Generation**: `POST /image/generate`
  - Parameters:
    - `prompt`: Text description for image generation

- **Root**: `GET /`
  - Returns a welcome message

## Project Structure

```
├── .env                  # Environment variables
├── main.py               # Application entry point
├── services.py           # API endpoint handlers
├── chat.py               # Chat functionality
├── photo.py              # Image generation functionality
├── utils.py              # Utility functions
├── requirements.txt      # Project dependencies
└── setup.bat             # Setup script for Windows
```
