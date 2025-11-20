import time

from playwright.sync_api import Playwright


class search_bar:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://dev.clinrol.com/")

    def navigate(self,data):
        self.page.get_by_role("button", name="Log in").click()
        self.page.locator("#email").fill(data['email'])
        self.page.locator("#password").fill(data['password'])
        self.page.get_by_role("button", name="Continue").click()
        overview = self.page.get_by_role("link", name="Overview")
        overview.wait_for(state = "visible")
        self.page.get_by_role("link", name="Patients").click()
        time.sleep(2)

    def search(self,data):

        self.page.get_by_placeholder("Search by patient").fill(data['patient_name'])
        time.sleep(2)
        trials = self.page.locator(
            "(//div[@class='flex flex-col md:flex-row md:items-center justify-between'])")
        count = trials.count()
        titles = self.page.locator(
            f"(//h3[@class ='font-medium text-gray-900 cursor-pointer hover:text-green-600 transition-colors'])")
        for i in range(count):
            title = titles.nth(i).text_content()

            assert  data['patient_name'].lower() in title.lower()

        time.sleep(2)
