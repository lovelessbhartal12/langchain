from langchain_community.document_loaders import csv_loader

loader=csv_loader(file_path='')
docs=loader.load()
print(len(docs))
