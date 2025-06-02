from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from typing import Optional
import google.generativeai as genai
import json
import os
from PIL import Image
import io

# إعداد API من Google
genai.configure(api_key="AIzaSyAjzM_BmIXGqMVVSGb1Lcu9-kMNO_1FmN8")

generation_config = {
    "temperature": 1,
    "top_k": 3,
    "top_p": 0.85,
    "max_output_tokens": 1024
}

safe = [
    {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_LOW_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_LOW_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_LOW_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_LOW_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_LOW_AND_ABOVE"},
]

system_instruction = """
You are an expert interior designer chatbot working in an app called 'Shatbly'.
You give friendly, personalized home design advice based on the user’s room type, style, color, and preferences.
Suggest ideas for layout, colors, furniture, and decor in a warm and helpful tone. Your name is MR Shatbly.
Use a lot of fitting emojis in every message . Start, end, and decorate your sentences with emojis that match the mood and topic 
. Be expressive and visually engaging 
, reduce asking.when user ask you in arabic resonse arabic
If you are asked about anything unrelated to furniture or interior design, kindly reply that you are a 'Shatbly'
 assistant specialized in interior and furniture consultations, and that you're here anytime to help with anything related 
 to home design .
"""

model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config,
    safety_settings=safe,
    system_instruction=system_instruction
)

app = FastAPI()

# CORS علشان الفرونت يقدر يتكلم مع الباك
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # عدل دي حسب الحاجة
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

HISTORY_FILE = "chat_history.json"

# تحميل تاريخ الشات من ملف
def load_chat_history():
    if os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

# حفظ تاريخ الشات
def save_chat_history(history):
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)

@app.post("/chat/")
async def chat_with_mrshatbly(
    message: str = Form(...),
    image: Optional[UploadFile] = File(None)
):
    history = load_chat_history()
    chat = model.start_chat(history=history)

    try:
        if image:
            contents = await image.read()
            pil_image = Image.open(io.BytesIO(contents)).convert("RGB")
            prompt_parts = [message, pil_image]
            response = chat.send_message(prompt_parts)
            history.append({"role": "user", "parts": [{"text": message}, {"text": "[Image sent]"}]})
        else:
            response = chat.send_message(message)
            history.append({"role": "user", "parts": [{"text": message}]})

        history.append({"role": "model", "parts": [{"text": response.text}]})
        save_chat_history(history)

        return JSONResponse(content={"response": response.text})
    except Exception as e:
        return JSONResponse(status_code=500, content={"error": str(e)})