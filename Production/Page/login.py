import time

from playwright.sync_api import Playwright, expect


class Login:
    def __init__(self, playwright:Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://www.clinrol.com/")
        self.page.get_by_role("button", name="Accept all").click()

    def navigate(self):
        self.page.get_by_role("button", name="Log in").click()

    def login(self, login_data):
        self.page.locator("#email").fill(login_data["user_email"])
        self.page.get_by_placeholder("Password").fill(login_data["user_password"])

        self.page.get_by_role("button", name="Continue").click()
        time.sleep(6)
        # expect(self.page.get_by_role("link", name="Overview")).to_be_visible()

        if self.page.get_by_role("link", name="Overview").is_visible():
            print(f"Test passed : {login_data['issue']}")
        else:
            print(f"Test failed : {login_data['issue']}")

    def forgetPassword(self, data):
        self.page.get_by_role("link", name="Forgot password?").click()
        self.page.get_by_placeholder("Enter your email address").fill(data['reset_email'])
        self.page.get_by_role("button", name="Send Reset Link").click()
        # text = self.page.locator("h2.font-bold")
        # text.wait_for(state="visible")
        email = data['reset_email']
        if email != "":
            self.page.get_by_role("link", name="Back to Sign In").wait_for(state="visible")
            self.page.get_by_role("link", name="Back to Sign In").click()
            self.page.locator("h2.mb-4").wait_for(state="visible")
        # expect(self.page.locator("h2.mb-4")).to_contain_text("Welcome to Clinrol")
        # self.page.locator("h2.mb-4").wait_for(state="visible")

        time.sleep(3)
        response = self.page.locator("h2.mb-4").text_content()
        if response == "Welcome to Clinrol":
            print(f"Test passed : {data['issue']}")
        else:
            print(f"Test failed : {data['issue']}")
        time.sleep(2)

