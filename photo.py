import httpx
import json
from fastapi import HTTPException
from pydantic import BaseModel, Field
from typing import Dict, Any
from utils import get_image_config

# Request and response models
class PromptRequest(BaseModel):
    prompt: str = Field(description="Text prompt describing the desired image")




class ImageResponse(BaseModel):
    image_data: str = Field(description="Base64 encoded image data")
    format: str = Field(description="Format of the image data")







def prepare_image_request(prompt: str, config: Dict[str, Any]) -> tuple[str, Dict[str, str], Dict[str, Any]]:
    """Prepare the API request URL, headers and payload for image generation"""
    # Build API URL
    base_url = config['base_url'] if config['base_url'].endswith('/') else f"{config['base_url']}/"
    api_url = f"{base_url}images/generations"
    
    # Prepare headers
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {config['api_key']}"
    }
    
    # Prepare payload
    payload = {
        "model": config['model'],
        "prompt": prompt,
        "n": 1,
        "size": f"{config['width']}x{config['height']}",
        "response_format": "b64_json"
    }
    
    return api_url, headers, payload





def process_image_response(response_data: Dict[str, Any]) -> Dict[str, str]:
    """Process successful API response and extract image data"""
    if 'data' in response_data and len(response_data['data']) > 0:
        image_item = response_data['data'][0]
        if 'b64_json' in image_item:
            return {
                "image_data": image_item['b64_json'],
                "format": "base64"
            }
    
    raise HTTPException(status_code=500, detail="No image data in response")






async def generate_image(prompt: str) -> Dict[str, Any]:
    """Generate an image based on the prompt using Nebius API"""
    try:
        # Get API configuration
        config = get_image_config()
        
        # Prepare request
        api_url, headers, payload = prepare_image_request(prompt, config)
        
        # Make API request
        async with httpx.AsyncClient() as client:
            response = await client.post(
                api_url,
                headers=headers,
                json=payload,
                timeout=60.0
            )
            
            # Process response
            if response.status_code == 200:
                return process_image_response(response.json())
            else:
                # Handle error response
                try:
                    error_data = response.json()
                    error_msg = f"API error: {json.dumps(error_data)}"
                except:
                    error_msg = f"API error with status code: {response.status_code}"
                
                raise HTTPException(status_code=response.status_code, detail=error_msg)
                
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image generation error: {str(e)}")
