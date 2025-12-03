import re
import time

from playwright.sync_api import Playwright, expect


class FilterByCondition:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://dev.clinrol.com/")
        self.page.get_by_role("button", name="Accept all").click()

    def navigate(self):
        self.page.get_by_role("button", name="Log in").click()
        self.page.locator("#email").fill("anish@gmail.com")
        self.page.locator("#password").fill("Password@123")
        self.page.get_by_role("button", name="Continue").click()
        time.sleep(2)
        self.page.locator("(//img[@class='hidden sm:block'])").click()
        self.page.get_by_role("link", name="Find a trial").click()

    def filter(self,data):
        self.page.get_by_role("link", name=data['disease']).first.click()
        time.sleep(2)
        trials = self.page.locator("div.flex.h-full")
        title = trials.nth(0).locator("h2.font-bold")
        expect(title).to_have_text(re.compile(data['disease'], re.IGNORECASE))
        print("Test Passed")
        time.sleep(2)