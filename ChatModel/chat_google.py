from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3-flash-preview",temperature=0.2,max_completion_tokens=10)
result = llm.invoke("Write a 5 line poem on cricket")
print(result)
print(result.content)