from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()

model=ChatAnthropic(model='claude-3-5-sonnet-2025555')

result=model.invoke('describe  me about the nepal')
print(result)