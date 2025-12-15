import time

from playwright.sync_api import Playwright, expect


class ImportSinglePatient:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://clinrol.com/")
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

    def import_single_patient(self,data):
        self.page.get_by_role("button", name="Import").click()
        self.page.get_by_role("menuitem", name="Add patient").click()
        dialog = self.page.get_by_role("dialog")
        dialog.locator("svg.lucide-chevron-down ").first.click()

        self.page.get_by_role("option", name=data["location"]).click()
        dialog.locator("//button[@aria-label='Select Country Code']").click()
        dialog.locator(f"//button[normalize-space()='{data['country_code']}']").click()
        dialog.locator("//button[@aria-label='Select Country Code']").click()
        dialog.get_by_placeholder("Enter phone number").fill(data['phone_number'])
        dialog.get_by_placeholder("Enter first name").fill(data['first_name'])
        dialog.get_by_placeholder("Enter last name").fill(data['last_name'])
        dialog.get_by_placeholder("Enter email address").fill(data['email'])
        dialog.locator("input[type='date']").fill(data['date'])
        dialog.locator("svg.lucide-chevron-down ").nth(1).click()
        # dialog.locator(f"div:has-text('{data['gender']}')").first.click()
        self.page.get_by_role("option", name=data["gender"]).first.click()
        dialog.locator("svg.lucide-chevron-down ").nth(2).click()
        # dialog.locator(f"div:has-text('{data['ethnicity']}')").first.click()
        self.page.get_by_role("option", name=data["ethnicity"]).click()
        dialog.get_by_placeholder("Enter ZIP code").fill(data['zip_code'])
        dialog.get_by_role("button", name="Add Patient").click()
        dialog.locator("svg.lucide-x").click()
        time.sleep(2)

        if self.page.locator(".Toastify__toast").is_visible():
            response = self.page.locator(".Toastify__toast").text_content()
            if response == "Patient added successfully!":
                print(f"Test passed : {response}")
                time.sleep(2)
                new_patient = self.page.locator("h3.font-medium").first
                expect(new_patient).to_contain_text(f"{data['first_name']}")
            else:
                print(f"Test failed : {response}")
        else:
            print("Test failed")



