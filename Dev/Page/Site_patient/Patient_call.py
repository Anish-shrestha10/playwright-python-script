
import time

from playwright.sync_api import Playwright, expect


class callPatient:
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

    def call_patient(self):
        trials = self.page.locator("(//div[@class='flex flex-col md:flex-row md:items-center justify-between'])").filter(has_text = "+9779843125788")
        trials.get_by_role("button", name="call").first.click()
        self.page.get_by_role("button", name="Start Call").click()
        ringing = self.page.get_by_text("Ringing")
        ringing.wait_for(state= "visible")
        expect(self.page.get_by_role("button", name="Ringing")).to_be_visible()
        time.sleep(5)
        self.page.get_by_role("button", name="Hang Up").click()
        time.sleep(3)