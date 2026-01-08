from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence
from dotenv import load_dotenv

load_dotenv()

prompts=PromptTemplate(
    template='write a joke about the topic:{topic}',
    input_variables=['topic']
)

model=ChatOpenAI()

parser=StrOutputParser()

 
chain=RunnableSequence(prompts , model , parser)

print(chain.invoke({'topic':'AI'}))