import time

from playwright.sync_api import Playwright, expect


class filterByStatus:
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

    def filter_by_status(self,data):
        self.page.get_by_role("button", name="Filter by Status").click()
        self.page.get_by_role("menuitemcheckbox").filter(has_text=f"{data['status']}").click()
        # trials = self.page.locator("(//div[@class='flex flex-col md:flex-row md:items-center justify-between'])")
        # count = trials.count()

        new_referral_labels = self.page.locator("div.inline-flex", has_text=f"{data['status']}")
        count = new_referral_labels.count()
        print(count)
        for i in range(count):
            assert new_referral_labels.nth(i).is_visible()
        time.sleep(3)