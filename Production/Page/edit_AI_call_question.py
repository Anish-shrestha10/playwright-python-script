import re
import time

from playwright.sync_api import Playwright, expect


class editAICallQuestion:
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

    def edit_AI_call_question(self,data):
        self.page.get_by_role("tab", name=re.compile(r"All trials", re.IGNORECASE)).click()
        time.sleep(3)

        self.page.get_by_placeholder("Search trials...").fill(data['trial'])
        self.page.locator("svg.lucide-ellipsis-vertical").first.click()
        self.page.get_by_text("Edit trial").first.click()
        question="gender?"
        self.page.get_by_text("AI call questions").click()
        time.sleep(2)

        question = "how are you?"
        question1 = "how are you??????"
        self.page.get_by_role("button", name="Add AI question").click()
        self.page.locator("#ai-question-text").fill(question)
        self.page.locator("#ai-question-criteria").fill(question)
        self.page.get_by_role("button", name="Add question").click()
        time.sleep(2)


        new_question = self.page.locator("div.p-3.gap-3").filter(has_text=question)
        new_question.locator("svg.lucide-pen-line").click()

        self.page.locator("#edit-ai-question-text").fill(question1)
        self.page.locator("#edit-ai-question-criteria").fill(question1)
        time.sleep(1)
        self.page.get_by_role("button", name="Save changes").click()
        # time.sleep(2)
        self.page.get_by_role("button", name="Save").click()
        time.sleep(3)
        new_question.locator("svg.lucide-trash2").click()
        time.sleep(2)
        self.page.get_by_role("button", name="Save").click()

        # expect(self.page.locator(".Toastify__toast")).to_contain_text("Trial updated successfully")

        response = self.page.locator(".Toastify__toast").text_content()
        if response == "Trial updated successfully":
            print("Test passed")
        else:
            print("Test failed")
        time.sleep(5)