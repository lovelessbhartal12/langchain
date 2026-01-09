from langchain_community.document_loaders import DirectoryLoader , PyPDFLoader

loader=DirectoryLoader(
    path='books',
    glob='*.pdf',
    loader_cls=PyPDFLoader


)
#loader()
docs=loader.load()

print(len(docs))
print(docs[0].page_content)
print(docs[0].metadata)

#lazy_loader()

docs=loader.lazy_load()

for document in docs:
    print(document.metadata)