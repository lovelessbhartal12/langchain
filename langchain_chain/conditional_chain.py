from langchain_openai import OpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.runnable import RunnableParallel # type: ignore
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel ,Field
from typing import Literal

load_dotenv()

model=ChatAnthropic()

parser=StrOutputParser() 

class feedback(BaseModel):
    sentences: Literal['positive' ,'negative']=Field(description='give the sentiment of the  feedbaack ')

parser2=PydanticOutputParser(pydantic_object=feedback)

prompt1=PromptTemplate(
    template='classify the sentiment of the following feedback text into positive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction ':parser2.get_format_instructions()}

)

classifer_chain= prompt1 | model | parser

