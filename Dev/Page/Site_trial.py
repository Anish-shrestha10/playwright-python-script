import re
import time


from playwright.sync_api import Playwright, expect


class siteTrial:
    def __init__(self,playwright:Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://dev.clinrol.com/")
        self.page.get_by_role("button", name="Accept all").click()

    def navigate(self,data):
        self.page.get_by_role("button", name="Log in").click()
        self.page.locator("#email").fill(data['email'])
        self.page.locator("#password").fill(data['password'])
        self.page.get_by_role("button", name="Continue").click()
        # self.page.get_by_role("link", name="Dashboard").click()
        time.sleep(1)

        self.page.get_by_role("link", name="Trials").click()

    def search_bar(self):
        self.page.get_by_placeholder("Search trials...").fill("SGLT2")
        time.sleep(2)
        expect(self.page.locator("div.font-semibold.tracking-tight").first).to_contain_text(
            re.compile("SGLT2", re.IGNORECASE)
        )
        time.sleep(5)
        self.page.get_by_placeholder("Search trials...").fill("")

    def Active_trial(self):

        # Using partial text match
        self.page.get_by_role("tab", name=re.compile(r"Active", re.IGNORECASE)).click()
        time.sleep(3)
        count = self.page.locator("div.items-start.gap-3").count()
        time.sleep(3)

        for i in range(0, count):
            # Get trial element
            trial_element = self.page.locator(
                f"(//div[contains(@class, 'flex items-center gap-2 flex-shrink-0')])[{i + 1}]")
            # (Optional) Wait for trial element to be visible/stable
            trial_element.wait_for(state="visible")
            # Extract trial status, assuming there is a label or text
            # Adjust selector according to your markup!
            for j in range(0,2):
                expect(self.page.locator(f"(//div[normalize-space()='Active'])[{j+1}]"))

    def Pending_trial(self):

        # Using partial text match
        self.page.get_by_role("tab", name=re.compile(r"Pending", re.IGNORECASE)).click()
        time.sleep(3)
        count = self.page.locator("div.items-start.gap-3").count()
        time.sleep(3)

        for i in range(0, count):
            # Get trial element
            trial_element = self.page.locator(
                f"(//div[contains(@class, 'flex items-center gap-2 flex-shrink-0')])[{i + 1}]")
            # (Optional) Wait for trial element to be visible/stable
            trial_element.wait_for(state="visible")
            # Extract trial status, assuming there is a label or text
            # Adjust selector according to your markup!
            for j in range(0,2):
                expect(self.page.locator(f"(//div[normalize-space()='Pending'])[{j+1}]"))






