from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough , RunnableLambda   
from dotenv import load_dotenv
load_dotenv()

prompt=PromptTemplate(
    template='write a joke about the {topic}',
    input_variables=['topic']
)
def word_count(text):
    return( len(text.split()))

 
model=ChatOpenAI()
parser=StrOutputParser()

joke_chian=RunnableSequence(prompt ,model , parser)

paralle_chian=RunnableParallel({
    'topic':RunnablePassthrough(),
     'word_count':RunnableLambda(word_count)
}
    

)

final_chian=RunnableSequence(joke_chian , paralle_chian)

final_result=final_chian.invoke({'topic':'volleyball'})

print(final_result)