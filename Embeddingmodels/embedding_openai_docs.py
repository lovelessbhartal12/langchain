from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()

embedding=OpenAIEmbeddings(
    model='text-embedding-3-large',
    dimensions=32
)
documents=[
    "delhi is the capital of india",
    "ktm is the capital of nepal",
    "i love you"
]

result=embedding.aembed_documents(documents) 

print(str(result))