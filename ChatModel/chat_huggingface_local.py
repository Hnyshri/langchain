from langchain_huggingface import ChatHuggingFace,HuggingFacePipeline
from dotenv import load_dotenv

load_dotenv()

lemModel = HuggingFacePipeline.from_model_id(
    repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",task="text-generation",
    pipeline_kwargs=dict({"temperature":0.2,"max_new_tokens":100}))

llm = ChatHuggingFace(llm=lemModel)
result = llm.invoke("Write a 5 line poem on cricket")
print(result)