from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview",temperature=1.5)

schema = [
    ResponseSchema(name="name", description="the name of the black hole"),
    ResponseSchema(name="distance", description="the distance of the black hole from earth"),
    ResponseSchema(name="size", description="the size of the black hole")
]
parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give me 5 facts about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction': parser.get_format_instructions()} # reutrn the JSON format instruction to the prompt
)

chain = template | model | parser
result = chain.invoke({'topic':'black hole'})

# promt = template.invoke({'topic':'black hole'}) 
# result = model.invoke(promt)
# result = parser.parse(result.content)

print(result)