import time

from playwright.sync_api import Playwright, expect

class HelpForm:
    def __init__(self,playwright:Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://dev.clinrol.com/")

    def navigate(self,data):
        self.page.get_by_role("button", name="Log in").click()
        self.page.locator("#email").fill(data['email'])
        self.page.locator("#password").fill(data['password'])
        self.page.get_by_role("button", name="Continue").click()
        time.sleep(2)

    def form(self,data):
        self.page.get_by_role("link", name="Help").click()
        self.page.get_by_placeholder("Enter full name").fill(data['fullname'])
        self.page.locator("//button[@aria-label='Select Country Code']").click()
        self.page.locator(f"//button[normalize-space()='{data['country_code']}']").click()
        self.page.locator("//button[@aria-label='Select Country Code']").click()
        self.page.get_by_placeholder("Enter your phone number").fill(data['number'])
        self.page.get_by_placeholder("Enter email address").fill(data['email'])
        self.page.select_option("(//select[@id='role'])",data['role'])
        self.page.get_by_placeholder("Your message...").fill(data['message'])
        self.page.get_by_role("checkbox").click()
        self.page.get_by_role("button", name="Send").click()
        expect(self.page.locator("div.Toastify__toast")).to_contain_text("Message sent successfully!")
        time.sleep(3)
