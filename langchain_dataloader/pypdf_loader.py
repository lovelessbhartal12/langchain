from langchain_community.document_loaders import PyPDFLoader


loader=PyPDFLoader('Deep Learning Curriculum (1).pdf')
docs=loader.load()
# print(len(docs))
print(docs[0].page_content)
