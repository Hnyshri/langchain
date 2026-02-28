from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage,AIMessage
import streamlit as st
load_dotenv()

#streamlit run Prompts/chatbot.py

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
col1, col2 = st.columns([4, 1])
with col1:
    st.title("🤖 AI Chatbot")
with col2:
    st.button("Clear",on_click=lambda: st.session_state.clear())


model = GoogleGenerativeAI(model="gemini-3.1-pro-preview",temperature=1.5)

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a helpful AI assistant.")
    ]

for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append(HumanMessage(content=user_input))

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.invoke(st.session_state.messages)
            st.markdown(response)

    st.session_state.messages.append(AIMessage(content=response))