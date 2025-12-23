import time

from playwright.sync_api import Playwright, expect


class Appointment:
    def __init__(self, playwright:Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://clinrol.com/")
        self.page.get_by_role("button", name="Accept all").click()

    def navigate(self,data):
        self.page.get_by_role("button", name="Log in").click()
        self.page.locator("#email").fill(data['email'])
        self.page.locator("#password").fill(data['password'])
        self.page.get_by_role("button", name="Continue").click()
        time.sleep(2)
        self.page.get_by_role("link", name= "Appointments").click()
        self.page.get_by_role("button", name="New appointment").click()

    def book_appointment(self,data):
        self.page.get_by_placeholder("Enter appointment title").fill(data['title'])
        self.page.locator("svg.lucide-chevron-down").nth(0).click()
        self.page.get_by_role("option", name=f"{data['type']}", exact=True).click()
        self.page.locator("(//input[@type='date'])").fill(data['date'])
        self.page.locator("svg.lucide-chevron-down").nth(1).click()
        self.page.get_by_role("option", name=f"{data['hour']}", exact=True).click()
        self.page.locator("svg.lucide-chevron-down").nth(2).click()
        self.page.get_by_role("option", name=f"{data['minute']}", exact=True).click()
        self.page.locator("svg.lucide-chevron-down").nth(3).click()
        self.page.get_by_role("option", name=f"{data['am/pm']}", exact=True).click()
        self.page.locator("svg.lucide-chevron-down").nth(4).click()
        self.page.get_by_role("option", name=f"{data['duration']}", exact=True).click()
        self.page.locator("svg.lucide-chevron-down").nth(5).click()
        self.page.get_by_role("option", name=f"{data['priority']}", exact=True).click()
        self.page.locator("//button[normalize-space()='Select patient...']").click()
        self.page.get_by_role("option", name=f"{data['patient']}").first.click()
        self.page.get_by_role("button", name="Add appointment").click()

        time.sleep(3)
        if self.page.locator(".Toastify__toast").is_visible():
            response = self.page.locator(".Toastify__toast").text_content()
            if response == "Appointment added successfully":
                print(f"Test passed : {response}")
            else:
                print(f"Test failed : {response}")
        else:
            print(f"Test failed")
        time.sleep(3)




