import time

from playwright.sync_api import Playwright, expect


class ConnectToTrial:
    def __init__(self, playwright:Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://www.clinrol.com/")

    def navigate(self,data):
        self.page.get_by_role("button", name="Log in").click()
        self.page.locator("#email").fill(data["email"])
        self.page.locator("#password").fill(data["password"])
        self.page.get_by_role("button", name="Continue").click()
        time.sleep(2)
        self.page.locator("(//img[@class='hidden sm:block'])").click()


    def search_trial(self):
        self.page.get_by_role("link", name="Find a trial").first.click()
        self.page.get_by_placeholder("Enter condition").fill("Post-operative Radiotherapy Omission in Selected Patients With Early Breast Cancer Trial")
        self.page.get_by_role("button", name="Search").click()
        time.sleep(5)
        self.page.locator("p.text-base").filter(has_text="Post-operative Radiotherapy Omission in Selected Patients With Early Breast Cancer Trial ...").click()
        self.page.get_by_role("button", name="Connect to trial").first.click()
        time.sleep(2)

    def QA_section(self):
        self.page.get_by_role("button", name="Get started").nth(1).click()

        self.page.locator("(//label)[1]").click()
        self.page.locator("(//label)[4]").click()
        self.page.locator("(//label)[6]").click()
        self.page.locator("(//label)[9]").click()
        self.page.locator("(//label)[10]").click()
        self.page.locator("(//label)[12]").click()
        self.page.locator("(//label)[14]").click()
        self.page.locator("(//label)[16]").click()
        self.page.locator("(//label)[18]").click()
        self.page.locator("(//label)[21]").click()
        self.page.locator("(//label)[23]").click()
        self.page.locator("(//label)[27]").click()

        for i in range(55):
            self.page.locator("(//*[name()='svg'])[3]").click()

        self.page.locator("(//label)[29]").click()
        self.page.locator("(//label)[34]").click()
        self.page.locator("(//label)[36]").click()
        self.page.get_by_role("button", name="Next").click()
        time.sleep(3)

    def patient_details(self,data):
        self.page.get_by_placeholder("Enter your first name").fill(data['first_name'])
        self.page.get_by_placeholder("Enter your last name").fill(data['last_name'])
        self.page.get_by_placeholder("Enter your email").fill(data['email'])
        self.page.get_by_role("button", name="Done").click()
        self.page.locator("//button[@aria-label='Select Country Code']//*[name()='svg']").click()
        self.page.locator("//button[normalize-space()='Nepal (+977)']").click()
        self.page.get_by_placeholder("Enter your phone number").fill(data['phone'])
        self.page.locator("//button[@aria-label='Select Country Code']//*[name()='svg']").click()
        self.page.locator("span.font-medium").nth(0).click()
        self.page.get_by_text("South Asian").click()
        self.page.locator("#zip-input").fill("3150")
        self.page.select_option("select", value=data['month'])
        self.page.get_by_placeholder("Day").fill(data['day'])
        self.page.get_by_placeholder("Year").fill(data['year'])
        self.page.locator("span.font-medium").nth(0).click()
        self.page.locator("(//li[normalize-space()='Female'])").click()
        self.page.locator("span.font-medium").nth(0).click()
        self.page.get_by_text("The Chris O'Brien Lifehouse").click()
        self.page.locator("(//input[@type='checkbox'])").click()
        self.page.get_by_role("button", name="Submit").click()
        time.sleep(1)
        expect(self.page.locator(".Toastify__toast")).to_contain_text("Application submitted successfully!")
        time.sleep(2)
