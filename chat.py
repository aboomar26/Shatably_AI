
import google.generativeai as genai
import PIL.Image
import os
import json

#  API
genai.configure(api_key="AIzaSyAjzM_BmIXGqMVVSGb1Lcu9-kMNO_1FmN8")

# generation_config
generation_config = {
    "temperature": 1,
    "top_k": 3,
    "top_p": 0.85,
    "max_output_tokens": 1024
}

# safety_settings
safe = [
    {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_LOW_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_LOW_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_LOW_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_LOW_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_LOW_AND_ABOVE"},
]

# system_instruction
system_instruction = """
You are an expert interior designer chatbot working in an app called 'Shatbly'.
You give friendly, personalized home design advice based on the user’s room type, style, color, and preferences.
Suggest ideas for layout, colors, furniture, and decor in a warm and helpful tone. Your name is Mandoh.

Use a lot of fitting emojis in every message . Start, end, and decorate your sentences with emojis that match the mood and topic 🖼️🌿. Be expressive and visually engaging 🎨!
, reduce asking.

If you are asked about anything unrelated to furniture or interior design, kindly reply that you are a 'Shatbly' assistant specialized in interior and furniture consultations, and that you're here anytime to help with anything related to home design 🏡✨.
"""

# MOdel Generation
model = genai.GenerativeModel(
    model_name="gemini-2.0-flash",
    generation_config=generation_config,
    safety_settings=safe,
    system_instruction=system_instruction
)

# chat_history
history_file = "chat_history.json"
chat_history = []
if os.path.exists(history_file):
    with open(history_file, "r") as f:
        try:
            chat_history = json.load(f)
        except json.JSONDecodeError:
            chat_history = []

chat = model.start_chat(history=chat_history)




# D:\Users\Darwish\PycharmProjects\Graduation_AI_API_\imagen1.png
image_path = r"".strip()  # ضع المسار هنا لو عايز تبعت صورة


while True:
    user_input = input("You: ").strip()
    if user_input:
        break


try:
    if image_path and os.path.exists(image_path):
        image = PIL.Image.open(image_path).convert("RGB")
        prompt_parts = [user_input, image]
        response = chat.send_message(prompt_parts)

        chat_history.append({"role": "user", "parts": [{"text": user_input}, {"text": "[Image sent]"}]})
    else:
        response = chat.send_message(user_input)
        chat_history.append({"role": "user", "parts": [{"text": user_input}]})

    chat_history.append({"role": "model", "parts": [{"text": response.text}]})
    print("Mandoh:", response.text)

    with open(history_file, "w") as f:
        json.dump(chat_history, f, indent=2)

except Exception as e:
    print(f"Error in initial message: {e}")


while True:
    user_input = input("You: ").strip()
    if not user_input:
        continue  # تجاهل الرسائل الفارغة
    if user_input.lower() in ["exit", "quit"]:
        print("Chat ended.")
        break

    try:
        response = chat.send_message(user_input)
        print("Mandoh:", response.text)

        chat_history.append({"role": "user", "parts": [{"text": user_input}]})
        chat_history.append({"role": "model", "parts": [{"text": response.text}]})

        with open(history_file, "w") as f:
            json.dump(chat_history, f, indent=2)
    except Exception as e:
        print(f"Error: {e}")

