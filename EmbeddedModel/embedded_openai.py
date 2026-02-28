from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = OpenAIEmbeddings(model="text-embedding-3-small",dimensions=32)
response = embeddings.embed_query("What is the capital of India?")  
print(str(response))