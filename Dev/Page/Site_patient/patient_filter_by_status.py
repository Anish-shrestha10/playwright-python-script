import time

from playwright.sync_api import Playwright, expect


class filterByStatus:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://dev.clinrol.com/")
        self.page.get_by_role("button", name="Accept all").click()

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
        status = self.page.locator("div.flex.items-center.cursor-pointer")
        count = status.count()
        print(count)
        for i in range(count):
            expect(status.nth(i)).to_contain_text(f"{data['status']}")
        time.sleep(3)