from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity

load_dotenv()

embedding = OpenAIEmbeddings(model = "text-embedding-3-large", dimensions = 100)

documents = [
    "MS dhoni is the best captain", 
    "Virat Kohli is the best player", 
    "Bumrah is known for his yorkers", 
    "UCF libary is nice"
]

query = "who is dhoni"

doc_embedings = embedding.embed_documents(documents)
q_embedding = embedding.embed_query(query)
