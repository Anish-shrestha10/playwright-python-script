
import re
import time

from playwright.sync_api import Playwright, expect


class editPhoneCall:
    def __init__(self,playwright:Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://clinrol.com/")

    def navigate(self,data):
        self.page.get_by_role("button", name="Log in").click()
        self.page.locator("#email").fill(data['email'])
        self.page.locator("#password").fill(data['password'])
        self.page.get_by_role("button", name="Continue").click()
        # self.page.get_by_role("link", name="Dashboard").click()
        time.sleep(1)

        self.page.get_by_role("link", name="Trials").click()

    def edit_phone_call(self,data):
        self.page.get_by_role("tab", name=re.compile(r"All trials", re.IGNORECASE)).click()
        time.sleep(3)

        self.page.get_by_placeholder("Search trials...").fill(data['trial'])
        self.page.locator("svg.lucide-ellipsis-vertical").first.click()
        self.page.get_by_text("Edit trial").first.click()
        question="Am i speaking to patient?"
        self.page.get_by_text("Phone call script").click()
        time.sleep(2)

        self.page.get_by_role("button", name="Add phone question").click()

        self.page.locator("#phone-question-text").fill(question)
        time.sleep(2)
        self.page.get_by_role("button", name="Add question").click()

        new_question = self.page.locator("div.p-3.gap-3").filter(has_text=question)
        new_question.locator("svg.lucide-pen-line").click()

        self.page.locator("#edit-phone-question-text").fill("Am i speaking to patient????")
        time.sleep(2)
        self.page.get_by_role("button", name="Save changes").click()

        self.page.get_by_role("button", name="Save").click()
        time.sleep(3)
        new_question.locator("svg.lucide-trash2").click()
        time.sleep(5)

        self.page.get_by_role("button", name="Save").click()

        # expect(self.page.locator(".Toastify__toast")).to_contain_text("Trial updated successfully")

        response = self.page.locator(".Toastify__toast").text_content()
        if response == "Trial updated successfully":
            print("Test passed")
        else:
            print("Test failed")
        time.sleep(5)