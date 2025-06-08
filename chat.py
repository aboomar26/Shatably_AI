import google.generativeai as genai
import json
import os
from PIL import Image
import io
from fastapi import HTTPException
from typing import Optional, List, Dict, Any
from utils import get_gemini_config, load_chat_history, save_chat_history

# Safety settings for Gemini
safe = [
    {"category": "HARM_CATEGORY_DANGEROUS", "threshold": "BLOCK_LOW_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_LOW_AND_ABOVE"},
    {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_LOW_AND_ABOVE"},
    {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_LOW_AND_ABOVE"},
    {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_LOW_AND_ABOVE"},
]





def initialize_gemini():
    """Initialize Gemini API with configuration"""
    config = get_gemini_config()
    genai.configure(api_key=config["api_key"])
    
    return genai.GenerativeModel(
        model_name=config["model"],
        generation_config=config["generation_config"],
        safety_settings=safe
    )





async def process_chat(message: str, image_data: Optional[bytes] = None, user_id: str = "default"):
    """Process a chat message with optional image"""
    try:
        # Initialize model and load config/history
        model = initialize_gemini()
        config = get_gemini_config()
        history = load_chat_history(user_id)
        
        # Start a new chat session
        chat = model.start_chat(history=[])
        
        # Apply system instruction
        system_instruction = config["system_instruction"]
        if system_instruction:
            try:
                # First try with system role
                try:
                    chat.send_message(system_instruction, role="system")
                except:
                    # If system role fails, try as user message
                    chat.send_message(f"You must act according to these instructions: {system_instruction}")
                    # Then send a confirmation message to verify
                    response = chat.send_message("Confirm that you understand and will follow these instructions.")
                    print(f"Bot confirmation: {response.text}")
            except Exception as e:
                print(f"Warning: Could not set system instruction: {str(e)}")
                
        # Process message with or without image
        if image_data:
            try:
                pil_image = Image.open(io.BytesIO(image_data)).convert("RGB")
                response = chat.send_message([message, pil_image])
                history.append({"role": "user", "parts": [{"text": message}, {"text": "[Image sent]"}]})
            except Exception as img_err:
                print(f"Error processing image: {str(img_err)}")
                raise HTTPException(status_code=400, detail=f"Failed to process image: {str(img_err)}")
        else:
            response = chat.send_message(message)
            history.append({"role": "user", "parts": [{"text": message}]})
        
        # Save response to history
        history.append({"role": "model", "parts": [{"text": response.text}]})
        save_chat_history(history, user_id)
        
        return {"response": response.text}
    
    except Exception as e:
        print(f"Error in process_chat: {str(e)}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))