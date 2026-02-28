from langchain_huggingface import HuggingFaceEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents = [
    "What is the capital of India?",
    "What is the capital of USA?",
    "What is the capital of France?"
]   
response = embeddings.embed_documents(documents)
print(str(response))
