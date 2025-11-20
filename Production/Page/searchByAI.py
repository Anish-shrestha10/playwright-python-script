import re
import time

from playwright.sync_api import Playwright, expect


class SearchByAI:
    def __init__(self, playwright:Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://www.clinrol.com/")

    def search(self,data):
        self.page.get_by_placeholder("Enter prompt or search by condition, age or location").fill(data['prompt'])
        self.page.get_by_role("button", name="Find Trials").click()
        time.sleep(3)
        trials = self.page.locator("div.flex.h-full")
        if trials == True:
            title = trials.nth(0).locator("h2.font-bold")
            expect(title).to_have_text(re.compile(data, re.IGNORECASE))
        time.sleep(5)
