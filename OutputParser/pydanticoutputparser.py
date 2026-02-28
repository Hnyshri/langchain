from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field

load_dotenv()

class Person(BaseModel):
    name: str = Field(description="the name of the person")
    age: int = Field(description="the age of the person",gt=18)
    city: str = Field(description="the city where the person lives")

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview",temperature=1.5)

parser = PydanticOutputParser(pydantic_object=Person)

template = PromptTemplate(
    template='Generate the name, age and city of a fictional {place} person \n {format_instruction}',
    input_variables=['place'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser
result = chain.invoke({'place':'sri lankan'})
print(result)
