from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import load_prompt

load_dotenv()

model = GoogleGenerativeAI( model="gemini-3-flash-preview",temperature=1.5)

st.header("Chat with AI")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need", "BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners", "Diffusion Models Beat GANs on Image Synthesis"] )
style_input = st.selectbox( "Select Explanation Style", ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"] ) 
length_input = st.selectbox( "Select Explanation Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"] )

template = load_prompt('Prompts/prompt_template.json')

# prompt = template.invoke({"paper_input": paper_input, "style_input": style_input, "length_input": length_input})
# if st.button("Submit"):
#     result = model.invoke(prompt)
#     st.write("AI Response:")
#     print(result)
#     st.write(result)


# Create the Chain of Thought Prompt Template and Model without calling invoke Fun
if st.button("Submit"):
    chain = template | model # Chain the prompt template and the model together
    result = chain.invoke({"paper_input": paper_input, "style_input": style_input, "length_input": length_input})
    st.write("AI Response:")
    st.write(result)
