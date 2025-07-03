from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

prompt_template = PromptTemplate.from_template("generate a deteiled prompt for a text-to-image model,skip the 'create' or 'generate' words, directly generate the description as if it a caption of the image. from this base prompt: {base_prompt}")

chain = prompt_template | llm

response = chain.invoke({"base_prompt": "a guy with a mustache"})
print(response.content)