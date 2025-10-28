from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0.4)

st.header("Research Assistant")

user_input = st.text_input("Enter your question")

if st.button('Get Answer'):
    result = model.invoke(user_input)
    st.write(result.content)