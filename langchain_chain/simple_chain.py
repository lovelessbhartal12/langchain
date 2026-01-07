from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser



load_dotenv()

prompt=PromptTemplate( 
    template='generate  5   interesting facts about {topic}', 
    input_variables=['topic']
)
 
model=OpenAI()
parser=StrOutputParser()

chain=prompt | model | parser

result=chain.invoke({'topic': ' cricket'})

print(result.content)

chain.get_graph().print_ascii()