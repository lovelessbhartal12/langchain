from langchain_community.retrievers import WikipediaRetriever

reteriver=WikipediaRetriever(top_k_results=2, lang="en")

query="The geopolitical history of nepal and chain from the perspective from the india "


docs=reteriver.invoke(query)

for i , doc in enumerate(docs):
    print(f"\n ........result {i+1}----")
    print(f"content:\n {doc.page_content}")