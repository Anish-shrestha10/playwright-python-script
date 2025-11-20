import time

from playwright.sync_api import Playwright, expect


class SiteOverview:
    def __init__(self, plawright:Playwright):
        self.browser = plawright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://dev.clinrol.com/")

    def navigate(self):
        self.page.get_by_role("button", name="Log in").click()
        self.page.locator("#email").fill("anish@gmail.com")
        self.page.locator("#password").fill("Password@123")
        self.page.get_by_role("button", name="Continue").click()
        time.sleep(2)

    def patient_view_all(self):
        self.page.get_by_role("button", name="View All").first.click()
        time.sleep(2)

        expect(self.page.locator("p.font-bold")).to_contain_text("Patients")
        self.page.get_by_role("link", name="Overview").click()

    def trials_view_all(self):
        self.page.get_by_role("button", name="View All").nth(1).click()
        time.sleep(2)

        expect(self.page.locator("p.font-bold")).to_contain_text("Clinical trials")
        time.sleep(2)
        self.page.get_by_role("link", name="Overview").click()

    def patient_details(self):
        patients_displayed = self.page.locator("//tbody/tr").count()
        for index in range(patients_displayed):
            # looping through tr
            print(patients_displayed)
            body = self.page.locator("tbody")
            row = body.locator("tr").nth(index)

            # gets to place where there is name and email of the patients, nth(1)= second td
            td = row.locator("td").nth(1)
            # get name of the patient
            name = td.locator("div.font-medium").first.text_content()
            print(name)

            # to click on action button
            row.locator("td").last.click()
            self.page.locator("//div[normalize-space()='View Details']").click()

            print(self.page.locator("h1.font-bold").text_content())
            expect(self.page.locator("h1.font-bold")).to_contain_text(name)
            time.sleep(2)
            self.page.locator("button.absolute").click()
            time.sleep(5)


    def edit_trial(self):
        self.page.get_by_role("link", name="Overview").click()
        self.page.locator("svg.lucide.lucide-ellipsis-vertical").first.click()
        time.sleep(1)
        self.page.get_by_text("Edit trial").click()

        time.sleep(3)
        expect(self.page.locator("//h1[@class='text-lg font-semibold whitespace-nowrap']")).to_contain_text("Edit Trial")
        time.sleep(2)