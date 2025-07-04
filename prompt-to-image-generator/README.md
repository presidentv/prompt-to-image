
# Prompt-to-Image Generator

This project creates a Streamlit app that generates a detailed image prompt from a base prompt and then generates an image based on that prompt using the Together API. The project also includes test scripts for the Together API and Groq API.

## Table of Contents

- [File Structure](#file-structure)
- [Setup](#setup)
- [Running the Streamlit App](#running-the-streamlit-app)
- [Test Scripts](#test-scripts)
  - [Test Together API](#test-together-api)
  - [Test Groq API](#test-groq-api)
  - [Test Groq with Langchain](#test-groq-with-langchain)
- [Example Generated Images](#example-generated-images)
- [Useful links](#useful_links)
- [Troubleshooting](#troubleshooting)

## File Structure

```
|->.venv
|->app
|      |->app.py
|->images
|->test
|      |->test_flux_api.py
|      |->test_groq_api.py
|      |->test_groq_langchain.py
|->.env
|->.gitignore
|->.python-version
```

- `app/app.py`: Main Streamlit app code.
- `images/`: Directory to store generated images.
- `test/test_flux_api.py`: Test script for the Together API.
- `test/test_groq_api.py`: Test script for the Groq API.
- `test/test_groq_langchain.py`: Test script for Groq with Langchain.
- `.env`: Environment variables file.
- `.gitignore`: Git ignore file.
- `.python-version`: Python version file.

## Setup

### 1. Create and Activate Virtual Environment

```bash
# Create virtual environment using uv (universal virtualenv)
uv .venv

# Activate the virtual environment
source .venv/bin/activate  # On macOS/Linux
.venv\Scripts\activate     # On Windows
```

### 2. Install Required Packages

```bash
pip install streamlit together langchain_groq langchain_core python-dotenv
```

### 3. Environment Variables

Create a `.env` file in the root directory and add your Together API key:

```
TOGETHER_API_KEY = your_api_key_here
GROQ_API_KEY = your_api_key_here
```

Replace `your_api_key_here` with your actual Together API key.

## Running the Streamlit App

To run the Streamlit app, use the following command:

```bash
streamlit run app/app.py
```

Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).

Certainly! Here is an expanded section for the test scripts, providing more detailed instructions and explanations for each test script included in your project.

---

## Test Scripts

The `test` directory contains several test scripts to validate different functionalities and APIs used in this project. Below are the detailed explanations and instructions for each test script.

### Test Together API

The `test/test_flux_api.py` script is used to test the Together API for generating images. This script performs the following steps:

1. **Import Required Libraries**: Import necessary libraries and modules such as `os`, `base64`, `time`, `Together`, and `dotenv`.
2. **Load Environment Variables**: Load the environment variables from the `.env` file using `load_dotenv()`.
3. **Create Together Client**: Initialize the Together client with the API key retrieved from the environment variables.
4. **Generate Image**: Call the `images.generate()` method with the prompt and other parameters to generate an image.
5. **Decode Image**: Decode the base64-encoded image data received in the response.
6. **Save Image**: Save the decoded image data to a file in the `images` directory with a unique filename based on the current timestamp.


### Test Groq API

The `test/test_groq_api.py` script tests the Groq API by sending a chat completion request and printing the response. The script performs the following steps:

1. **Import Required Libraries**: Import necessary libraries and modules such as `Groq` and `dotenv`.
2. **Load Environment Variables**: Load the environment variables from the `.env` file using `load_dotenv()`.
3. **Create Groq Client**: Initialize the Groq client.
4. **Create Chat Completion Request**: Send a chat completion request using the `chat.completions.create()` method with the desired model and message.
5. **Print Response**: Iterate through the response chunks and print the generated content.



### Test Groq with Langchain

The `test/test_groq_langchain.py` script uses Groq with Langchain to generate a detailed prompt for a text-to-image model. The script performs the following steps:

1. **Import Required Libraries**: Import necessary libraries and modules such as `ChatGroq` and `PromptTemplate` from `langchain_groq` and `langchain_core`.
2. **Initialize Language Model**: Create an instance of the `ChatGroq` model with the desired parameters.
3. **Define Prompt Template**: Define a prompt template using `PromptTemplate.from_template()` to generate a detailed prompt.
4. **Invoke Chain**: Create a chain by combining the prompt template and the language model, and invoke it with the base prompt.
5. **Print Response**: Print the generated detailed prompt.


---

These test scripts are designed to validate the core functionalities of generating images and interacting with the Groq API. Make sure you have the required environment variables set up in the `.env` file and that you activate your virtual environment before running the scripts.

## Example Generated Images
Below are some of the images generated using the Streamlit app and the Together API: 
### Image 1: fasion photo of a woman in a resort ![fasion photo](images/generated_image_1733525812.png)

## Useful Links

Here are some useful links that you can refer to for further information:

- [FLUX Prompt Generator](https://huggingface.co/spaces/gokaygokay/FLUX-Prompt-Generator)
- [FLUX Image Generator](https://api.together.ai/playground/image/black-forest-labs/FLUX.1.1-pro)
- [uv Documentation](https://docs.astral.sh/uv/)
- [Streamlit Documentation]([https://docs.streamlit.io/develop/api.html](https://docs.streamlit.io/develop/api-reference))
- [Together AI Documentation](https://docs.together.ai/docs/quickstart)
- [Groq Documentation](https://console.groq.com/docs/text-chat)
- [Groq API in LangChain](https://python.langchain.com/docs/integrations/chat/groq/)
- [LangChain Prompt Templates](https://python.langchain.com/docs/concepts/prompt_templates/)


## Troubleshooting

- **API Key Issues**: Ensure that the `TOGETHER_API_KEY` environment variable is correctly set in the `.env` file and loaded in your scripts.
- **Environment Activation**: Make sure you activate the virtual environment before running the scripts or the Streamlit app.
- **Dependencies**: Ensure all required packages are installed in the virtual environment.

