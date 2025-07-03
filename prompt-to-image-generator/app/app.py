import os
import base64
import time
import streamlit as st
from together import Together
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

# Load environment variables from .env file
load_dotenv()

# Create the Together client
client = Together(api_key=os.getenv("TOGETHER_API_KEY"))

# Initialize the language model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

# Define the prompt template
prompt_template = PromptTemplate.from_template(
    "generate a detailed prompt for a text-to-image model, skip the 'create' or 'generate' words, directly generate the description as if it is a caption of the image. from this base prompt: {base_prompt}"
)

# Streamlit app layout
st.title("Prompt-to-Image Generator")
base_prompt = st.text_input("Enter a base prompt:")

if st.button("Generate Image"):
    if base_prompt:
        # Generate detailed prompt using language model
        chain = prompt_template | llm
        response = chain.invoke({"base_prompt": base_prompt})
        detailed_prompt = response.content.strip()

        st.write("Generated Prompt:", detailed_prompt)

        # Generate the image
        response = client.images.generate(
            prompt=detailed_prompt,
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
        os.makedirs('../images', exist_ok=True)

        # Generate a unique filename using the current timestamp
        filename = f'../images/generated_image_{int(time.time())}.png'

        # Save the image to the 'images' folder
        with open(filename, 'wb') as file:
            file.write(image_data)

        st.image(filename, caption="Generated Image")
        st.write(f"Image saved to '{filename}'")
    else:
        st.warning("Please enter a base prompt.")
