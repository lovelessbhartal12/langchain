from langchain_openai import OpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1= PromptTemplate(
    template='generate the details report about :{topic}',
    input_variables=['topic']

)

prompt2= PromptTemplate(
    template='generate  5 point summary from teh  :{text}',
    input_variables=['text']

)

model=OpenAI()

parser=StrOutputParser()

chain= prompt1 | model | parser |prompt2 | model | parser

result=chain.invoke({'topic':'unpowerment women'})
print(result.content)