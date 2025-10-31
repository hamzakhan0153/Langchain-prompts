from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, AIMessage

chat_template = ChatPromptTemplate([
    ('system','You are an helpful {domian} expert.'),
    ('human','Explain in simpler words , what is {topic}')
])

prompt = chat_template.invoke({'domian':'cricket','topic':'dusra'})
print(prompt)
