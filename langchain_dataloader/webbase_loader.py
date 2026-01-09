from langchain_community.document_loaders import WebBaseLoader
url='https://www.daraz.com.np/products/mens-fleece-ninja-mask-hoodie-high-neck-cover-built-in-face-covering-i496296116-s2221709498.html?scm=1007.51610.379274.0&pvid=8ba42f01-6512-4cbe-a2fb-6f58ec8401d9&search=flashsale&spm=a2a0e.tm80335409.FlashSale.d_496296116'

loader=WebBaseLoader(url)

docs=loader.load()

print(len(docs))

print(docs[0].page_content)