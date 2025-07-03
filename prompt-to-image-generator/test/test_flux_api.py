import os
import base64
import time
from together import Together
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Create the Together client
client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

# Generate the image
response = client.images.generate(
    prompt="A beautiful sunrise over the mountains",  # Example prompt
    model="black-forest-labs/FLUX.1-schnell-Free",
    width=1024,
    height=768,
    steps=1,
    n=1,
    response_format="b64_json"
)

# Get the base64-encoded image
b64_image = response.data[0].b64_json

# Decode the base64 image
image_data = base64.b64decode(b64_image)

# Create the 'images' folder if it doesn't exist
os.makedirs('images', exist_ok=True)

# Generate a unique filename using the current timestamp
filename = f'images/generated_image_{int(time.time())}.png'

# Save the image to the 'images' folder
with open(filename, 'wb') as file:
    file.write(image_data)

print(f"Image saved to '{filename}'")
