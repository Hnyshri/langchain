from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model="gpt-5-nano",temperature=0.2,max_completion_tokens=10)
result = llm.invoke("Write a 5 line poem on cricket")
print(result)
print(result.content)