from browser import BrowserManager
from search import search_web
from extractor import PageExtractor
from writer import save_json
def main():
    query=input("Enter Search Query:")
    print("\nSearching...\n")
    urls=search_web(query)
    if not urls:
        print("No URLs Found")
        return
    browser=BrowserManager()
    browser.start()
    context=browser.new_context()
    extractor=PageExtractor(context)
    all_data=[]
    total=len(urls)
    for index,url in enumerate(urls,start=1):
        print(f"[{index}/{total}] Scraping:{url}")
        data=extractor.extract(url)
        if data:
            all_data.append(data)
    context.close()
    browser.stop()
    save_json(all_data)
    print("\nDone.")
if __name__ == "__main__":
    main()