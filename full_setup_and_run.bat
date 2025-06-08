@echo off
echo Starting full setup for Shatbly AI...

:: Step 1: Create virtual environment
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
) else (
    echo Virtual environment already exists.
)

:: Step 2: Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

:: Step 3: Install dependencies
echo Installing requirements...
pip install --upgrade pip
pip install -r requirements.txt

:: Step 4: Create .env file if not exists
if not exist ".env" (
    echo Creating default .env file...
    echo NEBIUS_API_KEY="API_key"> .env
    echo GEMINI_API_KEY="API_key">> .env
    echo TEMPERATURE=1>> .env
    echo TOP_K=3>> .env
    echo TOP_P=0.85>> .env
    echo MAX_OUTPUT_TOKENS=1024>> .env
    echo CHAT_MODEL=gemini-2.0-flash>> .env
    echo CHAT_HISTORY_FILE=chat_history.json>> .env
    echo SYSTEM_INSTRUCTION=You are an expert interior designer chatbot working in an app called 'Shatbly'. You give friendly, personalized home design advice based on the user's room type, style, color, and preferences. Suggest ideas for layout, colors, furniture, and decor in a warm and helpful tone. Your name is MR Shatbly. Use a lot of fitting emojis in every message. Start, end, and decorate your sentences with emojis that match the mood and topic. Be expressive and visually engaging, reduce asking. When user ask you in arabic resonse arabic. If you are asked about anything unrelated to furniture or interior design, kindly reply that you are a 'Shatbly' assistant specialized in interior and furniture consultations, and that you're here anytime to help with anything related to home design.>> .env
    echo IMAGE_MODEL=black-forest-labs/flux-schnell>> .env
    echo IMAGE_WIDTH=1024>> .env
    echo IMAGE_HEIGHT=1024>> .env
    echo IMAGE_STEPS=50>> .env
    echo IMAGE_BASE_URL=https://api.studio.nebius.com/v1/>> .env
    echo CORS_ORIGINS=["*"]>> .env
) else (
    echo .env file already exists.
)

:: Step 5: Run the application
echo Starting the application...
python main.py

pause
