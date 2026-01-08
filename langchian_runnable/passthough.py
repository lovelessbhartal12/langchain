from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough
from dotenv import load_dotenv
load_dotenv()

model=ChatOpenAI()

parser=StrOutputParser()

prompt=PromptTemplate(
    template='explain the joke about the :{topic}',
    input_variables=['topic']
)
prompt1=PromptTemplate(
    template='explain joke in a funny ways:{funny}',
    input_variables=['funny']
)

joke_generator_chain=RunnableSequence(prompt ,model ,parser)

parallel_chian=RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt1 ,model ,parser)
}
    
)

final_chian=RunnableSequence(joke_generator_chain , parallel_chian)

# final_chian.invoke({'topic'}:'nepal')

