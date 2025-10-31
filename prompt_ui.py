from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate,load_prompt

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0.4)

st.header("Research Assistant")

paper_input = st.selectbox( "Select Research Paper Name", ["Attention Is All You Need",
"BERT: Pre-training of Deep Bidirectional Transformers", "GPT-3: Language Models are Few-Shot Learners",
"Diffusion Models Beats GAN on image synthesis"] )

style_input = st.selectbox("Select Explaination Style", ["Beginner Friendly", "Technical Code-Oriented", "Mathematical"])

length_input = st.selectbox("Select Explaination Length", ["Short (1-2 paragraphs)", "Medium (3-5 paragraphs)", "Long (detailed explanation)"])

template = load_prompt('template.json')

    # prompt = template.invoke({
    #     'paper_input': paper_input,
    #     'style_input': style_input,
    #     'length_input': length_input
    # })

if st.button('Get Answer'):
    chain = template | model
    result = chain.invoke({
    'paper_input': paper_input,
    'style_input': style_input,
    'length_input': length_input
})
    #result = model.invoke(prompt)
    st.write(result.content)