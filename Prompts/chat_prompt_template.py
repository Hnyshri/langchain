from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

chat_template = ChatPromptTemplate([
    ('system','You are a helpful customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

chat_histories = []

with open('Prompts/prevoiusChat_database.txt','r') as f:
    chat_histories.extend(f.readlines())

print(chat_histories) 

prompt = chat_template.invoke({'chat_history': chat_histories, 'query': 'Where is my refund'})
print(prompt)