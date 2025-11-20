import time

from playwright.sync_api import Playwright, expect


class filterByTrail:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://clinrol.com/")

    def navigate(self,data):
        self.page.get_by_role("button", name="Log in").click()
        self.page.locator("#email").fill(data['email'])
        self.page.locator("#password").fill(data['password'])
        self.page.get_by_role("button", name="Continue").click()
        overview = self.page.get_by_role("link", name="Overview")
        overview.wait_for(state="visible")
        self.page.get_by_role("link", name="Patients").click()
        time.sleep(2)

    def filter_by_trail(self):
        self.page.get_by_role("button", name="Filter by trial").click()
        self.page.get_by_role("menuitem").filter(has_text = "Open label Study").click()

        trials = self.page.locator("(//div[@class='flex flex-col md:flex-row md:items-center justify-between'])", has_text = "Open label Study")
        count = trials.count()
        print(count)
        for i in range(count):
            assert trials.nth(i).is_visible()
        time.sleep(3)
