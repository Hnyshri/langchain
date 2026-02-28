from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

llm = ChatAnthropic(model="claude-sonnet-4-5-20250929",temperature=0.2,max_completion_tokens=10)
result = llm.invoke("Write a 5 line poem on cricket")
print(result)
print(result.content)