

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI(model = "gpt-4.1-nano")

# structure output Typed Dictornary

class Review(TypedDict):
    summary : str
    sentiment : str
    rating: int

structured_model = model.with_structured_output(Review)
review = """
The hardware is  not great, but the software feels bloated. There are too many pre-installed apps that I can't remove. Also, the UI looks outdated compared to other brands. Hoping for a software update to fix this. """

result = structured_model.invoke(review)
print(result)