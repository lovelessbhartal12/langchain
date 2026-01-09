# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import PromptTemplate
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough , RunnableLambda   
# from dotenv import load_dotenv
# load_dotenv()

# prompt=PromptTemplate(
#     template='write a joke about the {topic}',
#     input_variables=['topic']
# )
# def word_count(text):
#     return( len(text.split()))

 
# model=ChatOpenAI()
# parser=StrOutputParser()

# joke_chian=RunnableSequence(prompt ,model , parser)

# paralle_chian=RunnableParallel({
#     'topic':RunnablePassthrough(),
#      'word_count':RunnableLambda(word_count)
# }
    

# )

# final_chian=RunnableSequence(joke_chian , paralle_chian)

# final_result=final_chian.invoke({'topic':'volleyball'})

# print(final_result)
# value="hello world"
# def outer_function(x):

#  def inner_function():
#    print(value)

#  return inner_function()

# outer_function(value)

# def outer_function(fun):

#  def inner_function():

#   x =fun()

#  return inner_function()

# @outer_function

# def hello():
#   print('Hello world')

import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

def get_embedding(text, model="text-embedding-ada-002"):
    """Generate embedding for text"""
    text = text.replace("\n", " ")  # Replace newlines
    
    response = openai.Embedding.create(
        model=model,
        input=text
    )
    
    return response['data'][0]['embedding']

# Usage
text = "Python is a programming language"
embedding = get_embedding(text)
print(f"Embedding dimension: {len(embedding)}")  # 1536
print(f"First 5 values: {embedding[:5]}")