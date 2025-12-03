import time

from playwright.sync_api import Playwright, expect


class filterBySite:
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

    def filter_by_site(self,data):
        self.page.get_by_role("button", name="Filter by Site").click()
        self.page.get_by_role("menuitemcheckbox").filter(has_text=f"{data['site']}").click()
        time.sleep(2)
        trials = self.page.locator("(//div[@class='rounded-lg border text-card-foreground w-full max-w-full bg-transparent shadow-sm border-none overflow-hidden'])")
        count = trials.count()
        print(count)
        if count >0:
            for i in range(count):
                trial = self.page.locator("h3.font-medium").nth(i)
                trial.click()
                time.sleep(2)
                expect(self.page.locator("(//span[@class='font-medium text-sm sm:text-base break-words'])")).to_contain_text(f"{data['site']}")
                self.page.locator("svg.lucide-x").nth(1).click()
            time.sleep(3)
        else :
            print("No patient on this site")