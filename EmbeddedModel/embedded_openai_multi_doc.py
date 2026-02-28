from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small",dimensions=32)

documents = [
    "What is the capital of India?",
    "What is the capital of USA?",
    "What is the capital of France?"
]

response = embeddings.embed_documents(documents)  
print(str(response))