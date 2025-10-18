from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model = "gpt-3.5-turbo-instruct")

result = llm.invoke("How is the best indian cricket captian?, one word with name no extra info")

print(result)