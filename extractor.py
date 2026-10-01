from playwright.sync_api import TimeoutError
from config import TIMEOUT,MAX_SCROLLS,SCROLL_PAUSE
class PageExtractor:
    def __init__(self,context):
        self.context=context
    def extract(self,url):
        page=self.context.new_page()
        try:
            page.goto(url,wait_until="domcontentloaded",timeout=TIMEOUT )
            self.auto_scroll(page)
            result={
                "url": url,
                "title": page.title(),
                "blocks": []
            }
            blocks=page.evaluate("""
            ()=>{
                const output=[];
                const elements=document.querySelectorAll(
                    "h1,h2,h3,h4,h5,h6,p,a,img,button,pre,code,ul,ol"
                );
                elements.forEach(el =>{
                    const style=window.getComputedStyle(el);
                    if(
                        style.display==="none" ||
                        style.visibility==="hidden"
                    )
                        return;
                    const tag=el.tagName.toLowerCase();
                    const text=(el.innerText || "").trim();
                    if(tag==="img"){
                        output.push({
                            type:"image",
                            src:el.src,
                            alt:el.alt
                        });
                        return;
                    }
                    if(tag==="a"){
                        output.push({
                            type:"link",
                            text:text,
                            url:el.href
                        });
                        return;
                    }
                    if(tag==="button"){
                        output.push({
                            type:"button",
                            text:text
                        });
                        return;
                    }
                    if(tag==="pre"){
                        output.push({
                            type:"code",
                            code:text
                        });
                        return;
                    }
                    output.push({
                        type:tag,
                        text:text
                    });
                });
                return output;
            }
            """)
            result["blocks"]=blocks
            unique_blocks=[]
            seen=set()
            for block in result["blocks"]:
                key=str(block)
                if key not in seen:
                    seen.add(key)
                    unique_blocks.append(block)
            result["blocks"]=unique_blocks
            page.close()
            return result
        except TimeoutError:
            page.close()
            return{
                "url":url,
                "error":"Timeout",
                "blocks":[]
            }
        except Exception as e:
            page.close()
            return{
                "url":url,
                "error":str(e),
                "blocks":[]
            }
    def auto_scroll(self,page):
        previous_height=0
        for _ in range(MAX_SCROLLS):
            page.evaluate("""
                window.scrollTo(0,document.body.scrollHeight)
            """)
            page.wait_for_timeout(SCROLL_PAUSE)
            current_height=page.evaluate(
                "document.body.scrollHeight"
            )
            if current_height==previous_height:
                break
            previous_height=current_height
        page.evaluate(
            "window.scrollTo(0,0)"
        )
        page.wait_for_timeout(100)