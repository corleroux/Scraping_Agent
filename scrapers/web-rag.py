from langchain_community.document_loaders import (
    FireCrawlLoader,
)  # Importing the FireCrawlLoader

url = "https://firecrawl.dev"
loader = FireCrawlLoader(
    api_key="fc-YOUR_API_KEY",  # Note: Replace 'YOUR_API_KEY' with your actual FireCrawl API key
    url=url,  # Target URL to crawl
    mode="crawl",  # Mode set to 'crawl' to crawl all accessible subpages
)
docs = loader.load()

from langchain_community.embeddings import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
splits = text_splitter.split_documents(docs)
vectorstore = FAISS.from_documents(documents=splits, embedding=OllamaEmbeddings())


question = "What is firecrawl?"
docs = vectorstore.similarity_search(query=question)


from groq import Groq

client = Groq(
    api_key="YOUR_GROQ_API_KEY",
)

completion = client.chat.completions.create(
    model="llama3-8b-8192",
    messages=[
        {
            "role": "user",
            "content": f"You are a friendly assistant. Your job is to answer the users question based on the documentation provided below:\nDocs:\n\n{docs}\n\nQuestion: {question}",
        }
    ],
    temperature=1,
    max_tokens=1024,
    top_p=1,
    stream=False,
    stop=None,
)

print(completion.choices[0].message)
