from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOpenAI()

st.header("Chat with AI")

user_input = st.text_input("Enter your Prompt here:")

if st.button("Submit"):
    result = model(user_input)
    st.write("AI Response:")
    st.write(result.content)


# for run this file
# streamlit run Prompts/prompt_ui_streamlit.py