from fastapi import APIRouter, HTTPException, UploadFile, File, Form, status
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any
import traceback

# Import functions from modules
from chat import process_chat
from photo import generate_image, PromptRequest, ImageResponse

# Define response models
class ChatResponse(BaseModel):
    response: str = Field(description="The AI response to the user's message")

class ErrorResponse(BaseModel):
    error: str = Field(description="Error message")

# Create routers
chat_router = APIRouter(prefix="/chat", tags=["chat"])
image_router = APIRouter(prefix="/image", tags=["image"])







# Chat endpoint
# @chat_router.post("/",
#     response_model=ChatResponse,
#     responses={
#         status.HTTP_200_OK: {"model": ChatResponse, "description": "Successfully processed chat message"},
#         status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ErrorResponse, "description": "Internal server error"}
#     },
#     summary="Chat with AI interior design assistant",
#     description="Send a text message and optionally an image to get design advice from the AI assistant."
# )
# async def chat_endpoint(
#     message: str = Form(..., description="Text message to send to the AI assistant"),
#     image: Optional[UploadFile] = File(None, description="Optional image file to analyze"),
#     user_id: Optional[str] = Form("default", description="User identifier for chat history management")
# ):
#     """
#     Chat endpoint that processes messages and optional images
#
#     - **message**: Text message to send to the AI assistant
#     - **image**: Optional image file to analyze
#     - **user_id**: User identifier for chat history management
#
#     Returns a response from the AI assistant based on the input.
#     """
#     try:
#         # Process image if provided
#         image_data = None
#         if image:
#             image_data = await image.read()
#
#         # Process chat message
#         result = process_chat(message, image_data, user_id)
#         return JSONResponse(content=result)
#
#     except Exception as e:
#         return JSONResponse(
#             status_code=500,
#             content={"error": str(e)}
#         )


@chat_router.post("/",
    response_model=ChatResponse,
    responses={
        status.HTTP_200_OK: {"model": ChatResponse, "description": "Successfully processed chat message"},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ErrorResponse, "description": "Internal server error"}
    },
    summary="Chat with AI interior design assistant",
    description="Send a text message and optionally an image to get design advice from the AI assistant."
)
async def chat_endpoint(
    message: str = Form(..., description="Text message to send to the AI assistant"),
    image: UploadFile = File(None, description="Optional image file to analyze", media_type="image/*"),
    user_id: str = Form("default", description="User identifier for chat history management")
):
    """
    Chat endpoint that processes messages and optional images

    - **message**: Text message to send to the AI assistant
    - **image**: Optional image file to analyze
    - **user_id**: User identifier for chat history management

    Returns a response from the AI assistant based on the input.
    """
    try:
        # Process image if provided
        image_data = None
        if image:
            try:
                image_data = await image.read()
            except Exception as img_err:
                print(f"Error reading image: {str(img_err)}")
                return JSONResponse(
                    status_code=500,
                    content={"error": f"Failed to process image: {str(img_err)}"}
                )

        try:
            # Process chat message
            result = await process_chat(message, image_data, user_id)
            return JSONResponse(content=result)
        except Exception as chat_err:
            print(f"Error in chat processing: {str(chat_err)}")
            import traceback
            traceback.print_exc()
            return JSONResponse(
                status_code=500,
                content={"error": f"Chat processing failed: {str(chat_err)}"}
            )

    except Exception as e:
        print(f"Unexpected error in chat endpoint: {str(e)}")
        import traceback
        traceback.print_exc()
        return JSONResponse(
            status_code=500,
            content={"error": str(e) or "Unexpected error occurred"}
        )












# Image generation endpoint
@image_router.post("/generate",
    response_model=ImageResponse,
    responses={
        status.HTTP_200_OK: {"model": ImageResponse, "description": "Successfully generated image"},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": ErrorResponse, "description": "Internal server error"}
    },
    summary="Generate interior design image"
)
async def generate_image_endpoint(request: PromptRequest):
    """Generate an interior design image based on a text prompt"""
    try:
        result = await generate_image(request.prompt)
        return JSONResponse(content=result)
    
    except HTTPException as http_ex:
        return JSONResponse(
            status_code=http_ex.status_code,
            content={"error": http_ex.detail}
        )
    except Exception as e:
        return JSONResponse(
            status_code=500,
            content={"error": f"Image generation failed: {str(e)}"}
        )