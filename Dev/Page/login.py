import time

from playwright.sync_api import Playwright, expect


class Login:
    def __init__(self, playwright:Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://dev.clinrol.com/")

    def navigate(self):
        self.page.get_by_role("button", name="Log in").click()

    def login(self,login_data):
        self.page.locator("#email").fill(login_data["user_email"])
        self.page.get_by_placeholder("Password").fill(login_data["user_password"])

        self.page.get_by_role("button", name="Continue").click()
        time.sleep(2)
        expect(self.page.get_by_role("link", name="Overview")).to_be_visible()
        time.sleep(2)

    def forgetPassword(self):
        self.page.get_by_role("link", name="Forgot password?").click()
        expect(self.page.locator("h2.mb-4")).to_contain_text("Forgot Password?")

