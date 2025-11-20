import re
import time

from playwright.sync_api import Playwright, expect


class editPreScreening:
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

    def edit_pre_screening(self):
        self.page.get_by_role("tab", name=re.compile(r"All trials", re.IGNORECASE)).click()
        time.sleep(3)
        self.page.locator("svg.lucide-ellipsis-vertical").first.click()
        self.page.get_by_text("Edit trial").first.click()

        question = "What is your favourite food?"
        self.page.get_by_text("Pre-screening questions").click()
        self.page.get_by_role("button", name="Add question").click()
        time.sleep(3)
        expect(self.page.get_by_text("Add pre-screening question")).to_be_visible()

        self.page.locator("#question-text").fill(question)
        self.page.get_by_placeholder("Option 1").fill("MO:MO")
        self.page.get_by_role("checkbox").click()
        # page.get_by_role("button", name="Add option").click()
        self.page.locator("#question-criteria").fill(question)
        time.sleep(2)
        self.page.get_by_role("button", name="Add question").click()

        new_question = self.page.locator("div.p-3.gap-3").filter(has_text=question)

        # click on trash icon
        new_question.wait_for(state="visible", timeout=60000)
        new_question.locator("svg.lucide-pen-line").click()
        self.page.get_by_placeholder("Enter your criteria...").fill("are you a foodie?")
        time.sleep(2)
        # click on save changes inside edit card
        self.page.get_by_role("button", name="Save changes").click()
        time.sleep(2)

        # click on trash icon
        new_question.locator("svg.lucide-trash2").click()
        time.sleep(5)
        self.page.get_by_role("button", name="Save").click()

        expect(self.page.locator(".Toastify__toast")).to_contain_text("Trial updated successfully")
        time.sleep(5)