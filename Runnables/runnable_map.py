# Earlier used as mapping runnable. Now replaced with dictionary-based parallel execution:

from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableMap

load_dotenv()

model = GoogleGenerativeAI(model="gemini-3-flash-preview",temperature=1.5)
parser = StrOutputParser()

summary_prompt = PromptTemplate(
    template= "Summarize the following text:\n{text}",
    input_variables=['topic']
)

keywords_prompt = PromptTemplate(
    template=  "Extract 5 keywords from:\n{text}",
    input_variables=['text']
)

summary_chain = summary_prompt | model | parser
keywords_chain = keywords_prompt | model | parser

map_chain = RunnableMap({
    "summary": summary_chain,
    "keywords": keywords_chain
})

result = map_chain.invoke({"text": "AI is transforming industries..."})

print(result)