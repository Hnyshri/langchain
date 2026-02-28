from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()
current_dir = os.path.dirname(__file__)

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview",temperature=1.5)
parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a summary for the following poem - \n {poem}',
    input_variables=['poem']
)

file_path = os.path.join(current_dir, "cricket.txt")
loadText = TextLoader(file_path, encoding="utf-8")
docs = loadText.load()

print(docs)
print(docs[0].page_content)
print(docs[0].metadata)
print(type(docs[0]))
print(type(docs))
print(len(docs))

chain = prompt | model | parser
result = chain.invoke({ "poem" :docs[0].page_content})

print(result)