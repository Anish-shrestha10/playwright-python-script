import time

from playwright.sync_api import Playwright, expect


class ConnectToTrial:
    def __init__(self, playwright:Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://dev.clinrol.com/")
        self.page.get_by_role("button", name="Accept all").click()

    def navigate(self,data):
        self.page.get_by_role("button", name="Log in").click()
        self.page.locator("#email").fill(data['email'])
        self.page.locator("#password").fill(data['password'])
        self.page.get_by_role("button", name="Continue").click()
        time.sleep(2)
        self.page.locator("(//img[@class='hidden sm:block'])").click()


    def search_trial(self):
        self.page.get_by_role("link", name="Find a trial").first.click()
        self.page.get_by_placeholder("Enter condition").fill("SGLT2 Inhibitors As First Line Therapy to Prevent Renal Decline in Type 2 Diabetes")
        self.page.get_by_role("button", name="Search").click()
        time.sleep(5)
        self.page.locator("p.text-base").filter(has_text="SGLT2 Inhibitors As First Line Therapy to Prevent Renal Decline in Type 2 Diabetes").click()
        self.page.get_by_role("button", name="Connect to trial").first.click()
        time.sleep(2)

    def QA_section(self):
        time.sleep(2)
        count =  self.page.get_by_role("button", name="Get started").count()
        if count >= 2:
            self.page.get_by_role("button", name="Get started").nth(1).click()
        else:
            self.page.get_by_role("button", name="Get started").click()

        # for i in range(23):
        #     self.page.locator("(//*[name()='svg'])[3]").click()

        self.page.get_by_placeholder("Enter a number").first.fill("23")
        self.page.locator("(//label)[1]").click()
        self.page.locator("(//label)[4]").click()
        self.page.locator("(//label)[6]").click()
        # weight
        self.page.get_by_placeholder("Enter a number").nth(1).fill("50")

        # height
        self.page.get_by_placeholder("Enter a number").nth(2).fill("165")

        self.page.locator("(//label)[9]").click()
        self.page.locator("(//label)[12]").click()
        self.page.locator("(//label)[14]").click()
        self.page.locator("(//label)[16]").click()
        self.page.locator("(//label)[17]").click()
        self.page.locator("(//label)[19]").click()
        self.page.locator("(//label)[21]").click()

        # smoke count
        self.page.get_by_placeholder("Enter a number").nth(3).fill("1")

        self.page.locator("(//label)[22]").click()

        # eGFR count
        self.page.get_by_placeholder("Enter a number").nth(4).fill("20")



        self.page.get_by_role("button", name="Next").click()
        time.sleep(3)

    def patient_details(self,data):
        self.page.get_by_placeholder("Enter your first name").fill(data['first_name'])
        self.page.get_by_placeholder("Enter your last name").fill(data['Last_name'])
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
        self.page.locator("(//li[normalize-space()='Male'])").click()
        self.page.locator("span.font-medium").nth(0).click()
        self.page.get_by_text("The George Institute for Global Health").nth(1).click()
        self.page.locator("input.form-checkbox").click()
        self.page.get_by_role("button", name="Submit").last.click()
        time.sleep(1)
        response = self.page.locator(".Toastify__toast").first.text_content()
        if response =="Application submitted successfully!":
            print(f"Test passed : {response}")
        else :
            print(f"Test failed : {response}")
        time.sleep(2)
