from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model = "gemini-2.5-pro", temperature = 0.3)
result = model.invoke("Who is the best captain of INDIAN cricket team?, just one name top thats it")
print(result.content)
