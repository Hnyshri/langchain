# Wraps a normal Python function into a Runnable

from langchain_google_genai import GoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_core.runnables import RunnableLambda, RunnableSequence, RunnableParallel, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

def word_count(text:str) -> int:
    return len(text.split())

model = GoogleGenerativeAI(model="gemini-3-flash-preview",temperature=1.5)
parser = StrOutputParser()

prompt = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

joke_chain = RunnableSequence(prompt,model,parser)

parallel_chain = RunnableParallel({
     'joke': RunnablePassthrough(),
     'word_count': RunnableLambda(word_count)
})

runnable_lambda = RunnableSequence(joke_chain,parallel_chain)
result = runnable_lambda.invoke({'topic':'AI'})

print(result)

final_result = """ {}\n word Count - {}""".format(result['joke'],result['word_count'])
print(final_result)