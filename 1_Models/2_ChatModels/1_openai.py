from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
# can define the model type, api used, can also set temperature

model = ChatOpenAI(model = 'gpt-3',temperature = 0.3, max_completion_tokens= 20)
result = model.invoke("list the best ODI team of indian cricket team")

print(result.content)