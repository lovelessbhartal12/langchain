from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
 

# Step 1: Your source documents
docs= [
    Document(page_content="LangChain helps developers build LLM applications easily."),
    Document(page_content="Chroma is a vector database optimized for LLM-based search."),
    Document(page_content="Embeddings convert text into high-dimensional vectors."),
    Document(page_content="OpenAI provides powerful embedding models."),
]

embedding_model=OpenAIEmbeddings()

vector_store=Chroma(
    embedding_function=embedding_model,
    persist_directory="chromadb",
    collection_name="mycollection"

)
vector_store.add_documents(docs)
retriever=vector_store.as_retriever(search_kwargs={"k":2})

query="what is chorma used for"

result=retriever.invoke(query)

for i , doc in enumerate(result):
    print(f"\n ........result {i+1}----")
    print(f"content:\n {doc.page_content}")