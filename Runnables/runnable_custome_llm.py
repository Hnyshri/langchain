from abc import ABC, abstractmethod
import random

class Runnable(ABC):
    @abstractmethod
    def invoke():
        pass
    

class NakliLLM(Runnable):
    def __init__(self):
        print("NakliLLM initialized")
        
    def invoke(self,prompt):
        print(f"invoke for prompt: {prompt}")
        
        response_list = [
            'Delhi is the capital of India',
            'IPL is a cricket league',
            'AI stands for Artificial Intelligence'
        ]
        return {'response': random.choice(response_list)}
    
    def predict(self,prompt):
        print(f"Predicting for prompt: {prompt}")
        
        response_list = [
            'Delhi is the capital of India',
            'IPL is a cricket league',
            'AI stands for Artificial Intelligence'
        ]

        return {'response': random.choice(response_list)}
    
class NakliPromptTemplate(Runnable):
    def __init__(self,template,input_variables):
        self.template = template
        self.input_variables = input_variables
        print(f"NakliPromptTemplate initialized with template: {template} and input_variables: {input_variables}")
    
    
    def invoke(self, input_dict):
        return self.template.format(**input_dict)
    
    def format(self, input_dict):
        print(f"Formatting input: {input_dict}")
        return self.template.format(**input_dict)

class NakliStrOutputParser(Runnable):
    def __init__(self):
        pass
    
    def invoke(self, input_data):
        return input_data['response']
    
    
class RunnableConnetor(Runnable):
    
    def __init__(self,runnable_list):
        self.runnable_list = runnable_list
        
    def invoke(self, input_data):
        for runnable in self.runnable_list:
            input_data = runnable.invoke(input_data)
            
        return input_data

    
template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)

llm = NakliLLM()
strOutPutParser = NakliStrOutputParser()

chain = RunnableConnetor([template,llm,strOutPutParser])
result = chain.invoke({'length':'long', 'topic':'india'})
print(result)

template1 = NakliPromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

template2 = NakliPromptTemplate(
    template='Explain the following joke {response}',
    input_variables=['response']
)

chain1 = RunnableConnetor([template1,llm])
chain2 = RunnableConnetor([template2,llm,strOutPutParser])

main_chain = RunnableConnetor([chain1,chain2])
finalResult = main_chain.invoke({'topic':'cricket'})
print(finalResult)