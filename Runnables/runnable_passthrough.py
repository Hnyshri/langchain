# Passes input forward without modification
# from langchain_core.runnables import RunnablePassthrough

from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import RunnablePassthrough, RunnableSequence, RunnableParallel
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = GoogleGenerativeAI(model="gemini-3-flash-preview",temperature=1.5)
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

joke_chain = RunnableSequence(prompt1, model, parser)

parellel_chain = RunnableParallel({
    'joke' : RunnablePassthrough(),
    'explanation' : RunnableSequence(prompt2,model,parser)
})

final_chain = RunnableSequence(joke_chain, parellel_chain)

chain = final_chain.invoke({'topic':"AI"})

print(chain)