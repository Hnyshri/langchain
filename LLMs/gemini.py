from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv 

load_dotenv()

llm = GoogleGenerativeAI(model="gemini-3-flash-preview")
response = llm.invoke("What is the capital of India?")
print(response)