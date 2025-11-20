import re
import time

from playwright.sync_api import Playwright, expect


class SearchBar:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://dev.clinrol.com/")

    def navigate(self):
        self.page.get_by_role("button", name="Log in").click()
        self.page.locator("#email").fill("qa.site1.1@gmail.com")
        self.page.locator("#password").fill("Password@123")
        self.page.get_by_role("button", name="Continue").click()
        time.sleep(2)
        self.page.locator("(//img[@class='hidden sm:block'])").click()
        self.page.get_by_role("link", name="Find a trial").click()

    def search(self,searchdata):
        self.page.get_by_placeholder("Enter condition").fill(searchdata["condition"])
        self.page.get_by_placeholder("Enter location").fill(searchdata["place"])
        self.page.get_by_placeholder("Enter age").fill(searchdata["age"])
        self.page.get_by_role("button", name="Search").click()
        time.sleep(3)
        trials = self.page.locator("div.flex.h-full")
        title = trials.nth(0).locator("h2.font-bold")
        expect(title).to_have_text(re.compile(searchdata["condition"], re.IGNORECASE))
        location = trials.nth(0).locator("div.mb-2.flex.items-center.gap-1").nth(1)
        expect(location).to_have_text(re.compile(searchdata["place"], re.IGNORECASE))
        time.sleep(2)
