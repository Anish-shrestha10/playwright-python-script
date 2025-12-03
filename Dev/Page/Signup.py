import time

from playwright.sync_api import expect, Playwright


class Signup:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.context = self.browser.new_context()
        self.page = self.context.new_page()
        self.page.goto("https://dev.clinrol.com/")
        self.page.get_by_role("button", name="Accept all").click()

    def navigate(self):
        self.page.get_by_role("button", name="Get started").click()

    def signup(self, new_user):
        self.page.get_by_placeholder("First name").fill(new_user["first_name"])
        self.page.get_by_placeholder("Last name").fill(new_user["last_name"])
        self.page.get_by_placeholder("Email").fill(new_user["email"])

        self.page.locator("select").select_option(new_user["selectOption"])
        if new_user["selectOption"] in ["Site", "Sponsor"]:
            self.page.get_by_placeholder("Organisation name").fill(new_user["Organization"])

        self.page.get_by_placeholder("Create password").fill(new_user["password"])
        self.page.get_by_placeholder("Confirm password").fill(new_user["confirmPassword"])
        self.page.get_by_role("button", name="Create account").click()
        time.sleep(3)
        # expect(self.page.locator(".Toastify__toast")).to_contain_text("Account created successfully")
        if self.page.locator(".Toastify__toast").is_visible():
            response = self.page.locator(".Toastify__toast").text_content()
            if response == "Account created successfully! Please log in.":
                print(f"Test passed : {response}")
            else:
                print(f"Test failed : {response}")
        else:
            print(f"Test failed")
        time.sleep(5)
