from langchain_google_genai import GoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv

load_dotenv()

model = GoogleGenerativeAI( model="gemini-3-flash-preview",temperature=1.5)

messages = [
    SystemMessage(content="You are a helpful assistant that provides information about research papers."),
    HumanMessage(content="Can you explain the main contributions of the paper 'Attention Is All You Need'?"),
]

repsonse = model.invoke(messages)
messages.append(AIMessage(content=repsonse))
print(messages)