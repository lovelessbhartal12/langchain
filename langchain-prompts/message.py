from langchain_core.messages import SystemMessage , HumanMessage ,AIMessage
from langchain_openai import ChatOpenAI

from dotenv import load_dotenv
load_dotenv()


model=ChatOpenAI()

message=[
    SystemMessage(content='you are a helpful assistant'),
    HumanMessage(content='tell me about the langchian')

]

result=model.invoke(message)

message.append(AIMessage(content=result.content))