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
    echo NEBIUS_API_KEY=eyJhbGciOiJIUzI1NiIsImtpZCI6IlV6SXJWd1h0dnprLVRvdzlLZWstc0M1akptWXBvX1VaVkxUZlpnMDRlOFUiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiJnb29nbGUtb2F1dGgyfDExNTE3NDA1MzEwNDkyNDE1MTI2NSIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIiwiaXNzIjoiYXBpX2tleV9pc3N1ZXIiLCJhdWQiOlsiaHR0cHM6Ly9uZWJpdXMtaW5mZXJlbmNlLmV1LmF1dGgwLmNvbS9hcGkvdjIvIl0sImV4cCI6MTkwNDk4OTk0NCwidXVpZCI6ImE5YTIwNjlhLTM3ODktNDc3OC1iZGQ3LTg3MWVjMDA5YjRjOCIsIm5hbWUiOiJzYWh0YWJseSIsImV4cGlyZXNfYXQiOiIyMDMwLTA1LTE0VDExOjUyOjI0KzAwMDAifQ.v2v7T9Fdtwe2VSbD8YqYJ6N7gd5vR1nz3YWIQU26uV8> .env
    echo GEMINI_API_KEY=AIzaSyAjzM_BmIXGqMVVSGb1Lcu9-kMNO_1FmN8>> .env
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
