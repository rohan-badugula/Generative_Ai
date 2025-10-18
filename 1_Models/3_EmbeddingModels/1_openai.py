from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model='text-embedding-3-large', dimensions = 32)
# result = embedding.embed_query("Dhoni is the best captain")

documents = [
    "Hi I am Rohan",
    "How are you doning", 
    "I am a Data Scientist"
]

result = embedding.embed_documents(documents)
print(str(result))