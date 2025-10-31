from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

messages = [
    SystemMessage(content="You are a helpful research assistant."),
    HumanMessage(content="tell me about transformers")
]

response = model.invoke(messages)
messages.append(AIMessage(content=response.content))
print(messages)