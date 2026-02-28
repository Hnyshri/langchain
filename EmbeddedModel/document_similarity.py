from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
load_dotenv()

embeddings = OpenAIEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2",dimensions=300)

documents = [
    "Virat Kohli is an Indian cricketer known for his aggressive batting and leadership.",
    "MS Dhoni is a former Indian captain famous for his calm demeanor and finishing skills.",
    "Sachin Tendulkar, also known as the 'God of Cricket', holds many batting records.",
    "Rohit Sharma is known for his elegant batting and record-breaking double centuries.",
    "Jasprit Bumrah is an Indian fast bowler known for his unorthodox action and yorkers."
]

userQuery = 'tell me about Virat'

document_embedding = embeddings.embed_documents(documents)
user_embedding = embeddings.embed_query(userQuery)

scores = cosine_similarity([user_embedding],document_embedding)[0]

index, score= sorted(list(enumerate(scores)),key=lambda x:x[1][-1])

print(userQuery)
print(documents[index])
print("similarity score is:", score)