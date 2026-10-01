from ddgs import DDGS
from config import MAX_RESULTS
def search_web(query):
        urls=[]
    # with DDGS() as ddgs:
    #     results=ddgs.text(query,max_results=MAX_RESULTS)
    #     for result in results:
    #         href=result.get("href") or result.get("url")
    #         if href:
    #             urls.append(href)
    # return urls
        ddgs=DDGS()
        results=ddgs.text(query,max_results=MAX_RESULTS)
        for result in results:
            href=result.get("href") or result.get("url")
            if href:
                urls.append(href)
        return urls