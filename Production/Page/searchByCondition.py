import re
import time

from playwright.sync_api import Playwright, expect


class SearchByCondition:
    def __init__(self, playwright:Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://www.clinrol.com/")

    def search(self,data):
        self.page.get_by_text("Search by condition").click()
        self.page.get_by_placeholder("Cancer").fill(data['condition'])
        self.page.get_by_placeholder("Age").fill(data['age'])
        self.page.get_by_placeholder("Location").fill(data['location'])
        self.page.get_by_role("button", name="Find Trials").click()
        time.sleep(5)
        trials = self.page.locator("div.flex.h-full")
        title = trials.nth(0).locator("h2.font-bold")
        expect(title).to_have_text(re.compile(data['condition'], re.IGNORECASE))
        place = trials.nth(0).locator("div.mb-2.flex.items-center.gap-1").nth(1)
        expect(place).to_have_text(re.compile(data['location'], re.IGNORECASE))
        time.sleep(2)
