from playwright.sync_api import sync_playwright
from config import(HEADLESS,USER_AGENT,VIEWPORT_WIDTH,VIEWPORT_HEIGHT)
class BrowserManager:
    def __init__(self):
        self.playwright=None
        self.browser=None
    def start(self):
        self.playwright=sync_playwright().start()
        self.browser=self.playwright.chromium.launch(
            headless=HEADLESS,
            args=[
                "--disable-blink-features=AutomationControlled"
            ]
        )
    def new_context(self):
        return self.browser.new_context(
            viewport={
                "width":VIEWPORT_WIDTH,
                "height":VIEWPORT_HEIGHT
            },
            user_agent=USER_AGENT,
            ignore_https_errors=True
        )
    def stop(self):
        if self.browser:
            self.browser.close()
        if self.playwright:
            self.playwright.stop()

