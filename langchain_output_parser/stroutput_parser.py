from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate

from dotenv import load_dotenv
load_dotenv()

llm1=HuggingFaceEndpoint(repo_id="TinyLlama/TinyLama-1.1B-chat-v1.0" ,
                         task='text-generation')
model=ChatHuggingFace(llm=llm1)

# 1st prompt
template1=PromptTemplate(
    template='write a detailed report on {topic}',
    input_variables=['topic']

)

#2nd prompt
template2=PromptTemplate(
    template='write a five line summary on the following text /n {text}',
    input_variables=['text']


)

prompt1=template1.invoke({'topic':'Black hole'})
result=model.invoke(prompt1)

prompt2=template2.invoke({'text':result.content})

finalresult=model.invoke(prompt2)

print(finalresult.content )


