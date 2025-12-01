

import re
import time

from playwright.sync_api import Playwright, expect


class editTrial:
    def __init__(self,playwright:Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://dev.clinrol.com/")
        self.page.get_by_role("button", name="Accept all").click()

    def navigate(self,data):
        self.page.get_by_role("button", name="Log in").click()
        self.page.locator("#email").fill(data['email'])
        self.page.locator("#password").fill(data['password'])
        self.page.get_by_role("button", name="Continue").click()
        # self.page.get_by_role("link", name="Dashboard").click()
        time.sleep(1)

        self.page.get_by_role("link", name="Trials").click()

    def edit_trial(self,data):

        self.page.get_by_role("tab", name=re.compile(r"All trials", re.IGNORECASE)).click()
        time.sleep(3)
        self.page.get_by_placeholder("Search trials...").fill(data['trial'])
        self.page.locator("svg.lucide-ellipsis-vertical").first.click()
        self.page.get_by_text("Edit trial").first.click()
        time.sleep(3)
        self.page.locator("#start-date").fill(data['start_date'])
        self.page.locator("#end-date").fill(data['end_date'])
        self.page.locator("#target-enrollment").fill(data['target'])

        self.page.get_by_role("button", name="Add criteria").nth(0).click()
        self.page.get_by_placeholder("Enter inclusion criteria criterion...").last.fill(data['inclusive_question'])
        time.sleep(2)

        self.page.get_by_role("button", name="Add criteria").nth(1).click()
        self.page.get_by_placeholder("Enter exclusion criteria criterion...").last.fill(data['exclusion_question'])
        self.page.get_by_role("button", name="Save").click()
        time.sleep(3)

        # filter inclusion text that you want to delete and click on trash button
        del_inclusion = self.page.locator("div.flex.items-start").filter(
            has=self.page.locator(f"input[value={data['inclusive_question']}]"))
        del_inclusion.locator("svg.lucide-trash-2").click()

        # filter exclusion text that you want to delete and click on trash button
        del_exclusion = self.page.locator("div.flex.items-start").filter(
            has=self.page.locator(f"input[value={data['exclusion_question']}]"))
        del_exclusion.locator("svg.lucide-trash-2").click()
        time.sleep(1)
        self.page.get_by_role("button", name="Save").click()

        # expect(self.page.locator(".Toastify__toast")).to_contain_text("Trial updated successfully")
        response = self.page.locator(".Toastify__toast").text_content()
        if response == "Trial updated successfully":
            print("Test passed")
        else:
            print("Test failed")
        time.sleep(5)