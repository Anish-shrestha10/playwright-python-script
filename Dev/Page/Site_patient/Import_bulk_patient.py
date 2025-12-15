import time

from playwright.sync_api import Playwright, expect


class ImportBulkPatient:
    def __init__(self, playwright: Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://dev.clinrol.com/")
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

    def import_bulk_patient(self):
        self.page.get_by_role("button", name="Import").click()
        self.page.get_by_role("menuitem", name="Import from file").click()
        time.sleep(2)
        self.page.locator("input[type='file']").set_input_files("C:/Users/USER/Desktop/Clinrol automation/playwright-python-script/Test_patients_dev.csv")
        time.sleep(2)

        self.page.locator("#consent-checkbox").click()
        self.page.get_by_role("button", name="Import Applications").click()

        expect(self.page.locator(".Toastify__toast")).to_contain_text("Successfully imported")

