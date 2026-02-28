from langchain_huggingface import ChatHuggingFace,HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

lemModel = HuggingFaceEndpoint(repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",task="text-generation",temperature=0.2,max_new_tokens=10)

llm = ChatHuggingFace(llm=lemModel)
result = llm.invoke("Write a 5 line poem on cricket")
print(result)