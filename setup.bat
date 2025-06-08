@echo off
echo Setting up Shatably AI environment...

echo Creating virtual environment...
python -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate.bat

echo Installing dependencies...
pip install -r requirements.txt

echo Setup complete! You can now run the application with:
echo venv\Scripts\activate.bat

pause