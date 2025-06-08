import os
import json
from dotenv import load_dotenv
from typing import List, Dict, Any, Optional

# Load environment variables
load_dotenv()

# Environment variable getters
def get_env_var(var_name: str, default: Optional[str] = None) -> str:
    """
    Get environment variable with optional default value
    """
    value = os.getenv(var_name, default)
    if value is None or value.strip() == '':
        if default is not None:
            return default
        raise ValueError(f"Environment variable {var_name} not set and no default provided")
    return value

# Chat history management
def get_history_file_path(user_id: str = "default") -> str:
    """
    Get the path to the history file for a specific user
    """
    # Use chat_history directory for storing history files
    history_dir = "chat_history"
    history_file = get_env_var("HISTORY_FILE", "chat_history.json")
    base_filename = os.path.basename(history_file)
    
    # If user_id is provided, create a user-specific history file
    if user_id != "default":
        base, ext = os.path.splitext(base_filename)
        base_filename = f"{base}_{user_id}{ext}"
    
    # Combine directory and filename
    history_path = os.path.join(history_dir, base_filename)
    
    # Ensure the directory exists
    os.makedirs(history_dir, exist_ok=True)
    
    return history_path

def load_chat_history(user_id: str = "default") -> List[Dict[str, Any]]:
    """
    Load chat history from file for a specific user
    """
    history_file = get_history_file_path(user_id)
    
    if os.path.exists(history_file):
        with open(history_file, "r", encoding="utf-8") as f:
            try:
                history = json.load(f)
                # Ensure we only keep the last 20 messages
                if len(history) > 20:
                    history = history[-20:]
                return history
            except json.JSONDecodeError:
                return []
    return []

def save_chat_history(history: List[Dict[str, Any]], user_id: str = "default") -> None:
    """
    Save chat history to file for a specific user, keeping only the last 20 messages
    """
    # Ensure we only keep the last 20 messages
    if len(history) > 20:
        history = history[-20:]
        
    history_file = get_history_file_path(user_id)
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(history_file), exist_ok=True)
    
    with open(history_file, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=2, ensure_ascii=False)

# Configuration getters
def get_cors_origins() -> List[str]:
    """
    Get CORS origins from environment variable
    """
    origins_str = get_env_var("CORS_ORIGINS", "[\"*\"]")
    try:
        return json.loads(origins_str)
    except json.JSONDecodeError:
        return ["*"]

def get_gemini_config() -> Dict[str, Any]:
    """
    Get Gemini configuration from environment variables
    """
    try:
        return {
            "api_key": get_env_var("GEMINI_API_KEY"),
            "model": get_env_var("CHAT_MODEL", "gemini-2.0-flash"),
            "generation_config": {
                "temperature": float(get_env_var("TEMPERATURE", "1.0")),
                "top_k": int(get_env_var("TOP_K", "3")),
                "top_p": float(get_env_var("TOP_P", "0.85")),
                "max_output_tokens": int(get_env_var("MAX_OUTPUT_TOKENS", "1024")),
            },
            "system_instruction": get_env_var("SYSTEM_INSTRUCTION", "")
        }
    except ValueError as e:
        print(f"Error loading Gemini config: {str(e)}")
        # Return default configuration if there's an error
        return {
            "api_key": get_env_var("GEMINI_API_KEY"),  # This one must exist
            "model": "gemini-2.0-flash",
            "generation_config": {
                "temperature": 1.0,
                "top_k": 3,
                "top_p": 0.85,
                "max_output_tokens": 1024,
            },
            "system_instruction": ""
        }

def get_image_config() -> Dict[str, Any]:
    """
    Get image generation configuration from environment variables
    """
    return {
        "api_key": get_env_var("NEBIUS_API_KEY"),
        "base_url": get_env_var("NEBIUS_BASE_URL", "https://api.studio.nebius.com/v1/"),
        "model": get_env_var("IMAGE_MODEL", "black-forest-labs/flux-schnell"),
        "width": int(get_env_var("IMAGE_WIDTH", "520")),
        "height": int(get_env_var("IMAGE_HEIGHT", "520")),
        "steps": int(get_env_var("IMAGE_STEPS", "16")),
    }