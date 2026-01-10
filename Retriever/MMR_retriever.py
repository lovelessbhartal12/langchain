from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_core.documents import Document
import os
from langchain_community.vectorstores import FAISS


# Sample documents
docs = [
    Document(page_content="LangChain makes it easy to work with LLMs."),
    Document(page_content="LangChain is used to build LLM based applications."),
    Document(page_content="Chroma is used to store and search document embeddings."),
    Document(page_content="Embeddings are vector representations of text."),
    Document(page_content="MMR helps you get diverse results when doing similarity search."),
    Document(page_content="LangChain supports Chroma, FAISS, Pinecone, and more."),
]

embedding_model=OpenAIEmbeddings()

vector_store=FAISS.from_documents(
    documents=docs,
    embedding=embedding_model
)

retriever=vector_store.as_retriever(
    search_type="mmr",
    search_kwargs={"k":3,"lambd_mult":1}
)

query="what is langchain"
result=retriever.invoke(query)
