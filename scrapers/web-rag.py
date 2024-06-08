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
