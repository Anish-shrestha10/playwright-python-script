import time

from playwright.sync_api import Playwright, expect


class ClaimTrial:
    def __init__(self, playwright:Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://www.clinrol.com/")
        self.page.get_by_role("button", name="Accept all").click()

    def navigate(self,data):
        self.page.get_by_role("button", name="Log in").click()
        self.page.locator("#email").fill(data['email'])
        self.page.locator("#password").fill(data['password'])
        self.page.get_by_role("button", name="Continue").click()
        time.sleep(2)
        self.page.locator("(//img[@class='hidden sm:block'])").click()
        self.page.get_by_role("link", name="Find a trial").click()

    def search_trial(self,data):
        self.page.get_by_role("link", name="Find a trial").first.click()
        self.page.get_by_placeholder("Enter condition").fill(data['condition'])
        self.page.get_by_role("button", name="Search").click()
        self.page.locator("p.text-base").first.click()
        time.sleep(2)
        self.page.get_by_role("link", name="Claim this trial").first.click()
        time.sleep(2)

    def claim_trial_form(self,data):
        self.page.get_by_placeholder("Enter your first name").fill(data['firstname'])
        self.page.get_by_placeholder("Enter your last name").fill(data['lastname'])
        self.page.get_by_placeholder("Enter your email").fill(data['email'])
        self.page.get_by_placeholder("Enter your company").fill(data['company'])
        self.page.locator("//button[@aria-label='Select Country Code']//*[name()='svg']").click()
        self.page.locator(f"//button[normalize-space()='{data['country_code']}']").click()
        self.page.get_by_placeholder("Enter your phone number").fill(data['phone'])
        self.page.get_by_role("button", name ="Select an option").click()
        # time.sleep(2)
        self.page.locator("(//li[normalize-space()='Site'])").click()
        # time.sleep(2)
        self.page.get_by_placeholder("Search locations").click()
        # self.page.locator("div.m_92253aa5.mantine-Select-option.m_390b5f4").select_option(index=0)
        self.page.locator("[role='option']").nth(0).click()
        self.page.locator("(//input[@type='checkbox'])").click()
        self.page.get_by_role("button", name ="Submit").click()
        time.sleep(3)
        # expect(self.page.locator(".Toastify__toast")).to_contain_text("Application submitted successfully")
        if self.page.locator(".Toastify__toast").is_visible():
            response = self.page.locator(".Toastify__toast").text_content()
            if response == "Application submitted successfully":
                print(f"Test passed : {response}")
            else:
                print(f"Test failed : {response}")
        else:
            print(f"Test failed")
        time.sleep(5)