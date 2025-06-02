
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from openai import OpenAI
import base64
import os
from dotenv import load_dotenv

load_dotenv()

api_key = "eyJhbGciOiJIUzI1NiIsImtpZCI6IlV6SXJWd1h0dnprLVRvdzlLZWstc0M1akptWXBvX1VaVkxUZlpnMDRlOFUiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiJnb29nbGUtb2F1dGgyfDExNTE3NDA1MzEwNDkyNDE1MTI2NSIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIiwiaXNzIjoiYXBpX2tleV9pc3N1ZXIiLCJhdWQiOlsiaHR0cHM6Ly9uZWJpdXMtaW5mZXJlbmNlLmV1LmF1dGgwLmNvbS9hcGkvdjIvIl0sImV4cCI6MTkwNDk4OTk0NCwidXVpZCI6ImE5YTIwNjlhLTM3ODktNDc3OC1iZGQ3LTg3MWVjMDA5YjRjOCIsIm5hbWUiOiJzYWh0YWJseSIsImV4cGlyZXNfYXQiOiIyMDMwLTA1LTE0VDExOjUyOjI0KzAwMDAifQ.v2v7T9Fdtwe2VSbD8YqYJ6N7gd5vR1nz3YWIQU26uV8"


client = OpenAI(
    base_url="https://api.studio.nebius.com/v1/",
    api_key=api_key
)

app = FastAPI()

# CORS settings to allow frontend calls
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can restrict this in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class PromptRequest(BaseModel):
    prompt: str

@app.post("/generate")
def generate_image(request: PromptRequest):
    try:
        response = client.images.generate(
            model="black-forest-labs/flux-schnell",
            response_format="b64_json",
            prompt=request.prompt,
            extra_body={
                "response_extension": "png",
                "width": 520,
                "height": 520,
                "num_inference_steps": 16,
                "negative_prompt": "",
                "seed": -1
            }
        )

        if response.data:
            b64_image = response.data[0].b64_json
            return {"image_base64": b64_image}
        else:
            raise HTTPException(status_code=500, detail="Invalid response from API.")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
