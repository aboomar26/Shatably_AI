from openai import OpenAI
import base64
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Retrieve the API key from the environment variable
api_key = "eyJhbGciOiJIUzI1NiIsImtpZCI6IlV6SXJWd1h0dnprLVRvdzlLZWstc0M1akptWXBvX1VaVkxUZlpnMDRlOFUiLCJ0eXAiOiJKV1QifQ.eyJzdWIiOiJnb29nbGUtb2F1dGgyfDExNTE3NDA1MzEwNDkyNDE1MTI2NSIsInNjb3BlIjoib3BlbmlkIG9mZmxpbmVfYWNjZXNzIiwiaXNzIjoiYXBpX2tleV9pc3N1ZXIiLCJhdWQiOlsiaHR0cHM6Ly9uZWJpdXMtaW5mZXJlbmNlLmV1LmF1dGgwLmNvbS9hcGkvdjIvIl0sImV4cCI6MTkwNDk4OTk0NCwidXVpZCI6ImE5YTIwNjlhLTM3ODktNDc3OC1iZGQ3LTg3MWVjMDA5YjRjOCIsIm5hbWUiOiJzYWh0YWJseSIsImV4cGlyZXNfYXQiOiIyMDMwLTA1LTE0VDExOjUyOjI0KzAwMDAifQ.v2v7T9Fdtwe2VSbD8YqYJ6N7gd5vR1nz3YWIQU26uV8"
# Ensure the API key is loaded
if api_key is None:
    raise ValueError("API key not found in the environment")

# Set up the client using the loaded API key
client = OpenAI(
    base_url="https://api.studio.nebius.com/v1/",
    api_key=api_key  # Use the loaded API key
)

# model = "stability-ai/sdxl"
# model = "black-forest-labs/flux-dev"
# model = "black-forest-labs/flux-schnell"

def generate_image(prompt):
    try:
        response = client.images.generate(
            model="black-forest-labs/flux-schnell",
            response_format="b64_json",  # استخدم b64_json عشان تقدر تفك وتحفظ الصورة
            prompt=prompt,
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
            #  Base6
            b64_image = response.data[0].b64_json
            image_data = base64.b64decode(b64_image)

            #  PNG saving
            # dict = generated_image.png
            file_path = "generated_image.png"
            with open(file_path, "wb") as f:
                f.write(image_data)

            print(f"Image saved locally as '{file_path}'")
            return file_path
        else:
            print("Invalid response from the server.")
            return None

    except Exception as e:
        print(f"Error generating image: {str(e)}")
        return None

# Testing
user_prompt = input("Enter the image description: ")
file_path = generate_image(user_prompt)

if file_path:
    print("Done Check your image.")
else:
    print("Failed to generate the image.")
