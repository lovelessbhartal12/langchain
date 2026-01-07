from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

from dotenv import load_dotenv
load_dotenv()

llm1=HuggingFaceEndpoint(repo_id="TinyLlama/TinyLama-1.1B-chat-v1.0" ,task='text-generation')

model=ChatHuggingFace(llm=llm1)
parser=JsonOutputParser()
tempalte1=PromptTemplate(
    template='give me the name ,age ,city   of a fictional person \n {format_inst}',
    input_variables=[],

    partial_variables={'format_inst':  parser.get_format_instructions( )}
)

promt=tempalte1.format()

result=model.invoke(promt)
final_Result=parser.parse(result.content)


print(final_Result)
  