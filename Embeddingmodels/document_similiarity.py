from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

embedding=OpenAIEmbeddings(model='text-embedding-3-large' , dimensions=300)

document=[
    "virat kholi is an indian circkter known for his aggresive cricket batting and leadership",
    "ms dhoni is a former indain crickter famous for his calm demeaor and finishing skills",
    "sachin tendulkar also known as 'god of circket' holds many batting records ",
    "jasprit bumrah is an indian fast boller know for his yoker" 
]

query='tell me about the virat kholi'

doc_embeddding=embedding.aembed_documents(document)

query_embedding=embedding.aembed_query(query)

score=cosine_similarity([query_embedding],[doc_embeddding])

index ,score=sorted(list(enumerate(score)) , key=lambda x:x[1])[-1]

print(query)
print(document[index])
