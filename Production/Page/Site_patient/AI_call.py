
import time

from playwright.sync_api import Playwright, expect


class AiCall:
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

    def ai_call_patient(self):
        trials = self.page.locator(
            "(//div[@class='flex flex-col md:flex-row md:items-center justify-between'])").filter(
            has_text="+9779843125788")
        trials.get_by_role("button", name="AI Call").first.click()
        self.page.get_by_role("button", name = "Call now").click()
        time.sleep(3)
        expect(self.page.get_by_text("Preparing AI call")).to_be_visible()

    def ai_call_schedule(self,data):
        trials = self.page.locator(
            "(//div[@class='flex flex-col md:flex-row md:items-center justify-between'])").filter(
            has_text="+9779843125788")
        trials.get_by_role("button", name="AI Call").first.click()
        self.page.locator("input[type='date']").fill(data['date'])

        time_picker = self.page.locator("(//div[contains(@class,'flex gap-2')])[3]")
        # for Hour
        time_picker.locator("svg.lucide-chevron-down.h-4").nth(0).click()
        self.page.get_by_role("option", name=f"{data['hr']}").click()

        # for min
        time_picker.locator("svg.lucide-chevron-down.h-4").nth(1).click()
        self.page.get_by_role("option", name=f"{data['min']}").click()

        # for AM/PM
        time_picker.locator("svg.lucide-chevron-down.h-4").nth(2).click()
        self.page.get_by_role("option", name=f"{data['am/pm']}").click()

        self.page.get_by_role("button", name="Schedule call").click()

        # expect(self.page.locator("div.Toastify__toast")).to_contain_text("AI call scheduled successfully")

        response = self.page.locator(".Toastify__toast").text_content()
        if response == "AI call scheduled successfully":
            print("Test passed")
        else:
            print("Test failed")
        time.sleep(3)
