import os, re

from crewai.tools import tool
from firecrawl import FirecrawlApp, ScrapeOptions

@tool
def web_search_tool(query:str):
    '''
    Docstring for web_search_tool
    
    :param query: Description
    :type query: str
    '''
    app  = FirecrawlApp(api_key=os.getenv("FIRECRAWL_API_KEY"))

    response = app.search(
        query=query,
        scrape_options=ScrapeOptions(
            formats=["markdown"],
        ),
        limit=5,
    )

    if not response.success:
        return "Error using tool: " + response.error_message
    
    cleaned_chunks = []
    
    for result in response.data:
        
        title = result["title"]
        url = result["url"]
        markdown = result["markdown"]

        cleaned = re.sub(r"\\+|\n+", "", markdown).strip()
        cleaned = re.sub(r"\[[^\]]+\]\([^\)]+\)|https?://[^\s]+", "", cleaned)

        cleaned_result = {
            'title': title,
            'url': url,
            'content': cleaned,
        }

        cleaned_chunks.append(cleaned_result)

    return cleaned_chunks
