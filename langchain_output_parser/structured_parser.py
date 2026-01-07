# from langchain_huggingface import ChatHuggingFace , HuggingFaceEndpoint
# from langchain_core.prompts import PromptTemplate  
# from langchain.output_parsers import StructuredOutputParser ,ResponseSchema

# # Example

# from dotenv import load_dotenv
# load_dotenv()

# llm1=HuggingFaceEndpoint(repo_id="TinyLlama/TinyLama-1.1B-chat-v1.0" ,task='text-generation')

# model=ChatHuggingFace(llm=llm1)

# schema=[
#     ResponseSchema(name='fact_1', descritpion='fact_1 about the topic')
#     ResponseSchema(name='fact_2', descritpion='fact_2 about the topic')
#     ResponseSchema(name='fact_3', descritpion='fact_3 about the topic')
#     ]

# parser=StructuredOutputParser.from_response_schema(schema)

# template=PromptTemplate(
#     template='give me three facts abou the {topic} \n {format_instruction}',
#     input_variables=['topic'],
#     partial_variables={'format_instruction': parser.get_format_instruction()}


# )

# prompt=template.invoke({'topic':'about nepal'})
# result=model.invoke(prompt)

# final_result=parser.parse(result.content)

# print(final_result)