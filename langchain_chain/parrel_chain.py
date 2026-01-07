from langchain_openai import OpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel
load_dotenv()

model1=OpenAI()
model2=ChatAnthropic(model_name='claude-3')

promtpt1=PromptTemplate(
    template='generate the short and simple notes from :{text}',
    input_variables=['text']
)

promtpt2=PromptTemplate(
    template='generate the 5 mcq question from :{text}',
    input_variables=['text']
)

promtpt3=PromptTemplate(
    template='merge the provided notes and ,mcq in the single text : \n {notes} and quiz{quiz}',
    input_variables=['notes','quiz']
)


parser=StrOutputParser()



parallel_chain=RunnableParallel( { 
    'notes': promtpt1 | model1| parser,
    'quiz':promtpt2 |model2 | parser

})

merge_chain=promtpt3 | model2 | parser

chain= parallel_chain | merge_chain

result=chain.invoke()