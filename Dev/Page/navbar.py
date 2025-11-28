import time

from playwright.sync_api import Playwright, expect


class Navbar:
    def __init__(self, playwright:Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://dev.clinrol.com/")
        self.page.get_by_role("button", name="Accept all").click()

    def check_navbar(self):
        # logo
        self.page.get_by_role("button", name="Log in").click()
        time.sleep(2)
        self.page.locator("//a[@class='lg:mr-8 xl:mr-14']").click()
        time.sleep(2)
        expect(self.page.locator("h1.text-3xl")).to_contain_text("Find tomorrow's")

        # find a trial
        self.page.get_by_role("link", name="Find a trial").first.click()
        time.sleep(3)
        expect(self.page.locator("h1.font-semibold")).to_contain_text("Find a clinical trial near you")

        # researchers
        self.page.get_by_role("link", name="Researchers").click()
        time.sleep(2)
        expect(self.page.locator(
            "//h1[normalize-space()='Simplify how you recruit and connect with patients']")).to_be_visible()

        # sponsores
        self.page.get_by_role("link", name="Sponsors").click()
        time.sleep(2)
        expect(self.page.locator("h1.text-coolGray-900")).to_contain_text("Patient recruitment for sponsors")

        # patients
        self.page.get_by_role("link", name="Patients").click()
        time.sleep(2)
        expect(self.page.locator("h1.text-coolGray-900")).to_contain_text("Clinical trials for patients")

        # company
        self.page.get_by_role("link", name="Company").click()
        time.sleep(2)
        expect(self.page.locator("p.mb-4")).to_contain_text("Let's work together to solve today's biggest challenges in clinical trials. ")

        # login
        self.page.get_by_role("button", name="Log in").click()
        time.sleep(2)
        expect(self.page.locator("p.mb-12")).to_contain_text("Log in below to continue ")

        # signup
        self.page.get_by_role("button", name="Get started").click()
        time.sleep(2)
        expect(self.page.locator("h2.mb-4")).to_contain_text("Create your free account")