import time

from playwright.sync_api import Playwright, expect

class Homepage:
    def __init__(self, playwright:Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://clinrol.com/")
        self.page.get_by_role("button", name="Accept all").click()

    def browse_by_condition(self,data):
        self.page.get_by_role("button", name=f"{data['condition']}").click()
        time.sleep(3)
        conditions = self.page.locator("span.line-clamp-1").count()
        print(conditions)
        for i in range(conditions):
            title = self.page.locator("span.line-clamp-1").nth(i).text_content()
            # print(title)
            assert data['condition'].lower() in title.lower()

        self.page.get_by_role("button", name="View all trials →").click()
        time.sleep(3)
        expect(self.page.locator("(//h1[normalize-space()='Find a clinical trial near you'])")).to_be_visible()

    def how_clinrol_works_section(self):
        self.page.go_back()

        self.page.get_by_role("button", name="Find a trial").nth(1).click()
        time.sleep(3)
        expect(self.page.locator("(//h1[normalize-space()='Find a clinical trial near you'])")).to_be_visible()
        self.page.go_back()
        self.page.get_by_role("button", name="Find or engage patients").nth(0).click()
        time.sleep(2)
        expect(self.page.locator(
            "//h1[normalize-space()='Simplify how you recruit and connect with patients']")).to_be_visible()

    def how_clinrol_helps_sponsors_sites(self):
        self.page.go_back()
        self.page.get_by_role("button", name="Contact our team").click()
        time.sleep(3)
        expect(self.page.locator("h1.font-bold")).to_contain_text("Get in touch with Clinrol")
        self.page.go_back()
        self.page.get_by_role("button", name="Find Patients").click()
        time.sleep(3)
        expect(self.page.locator("h1.text-coolGray-900")).to_contain_text("Clinical trials for patients")

    def trusted_by_over_100k_section(self,data):
        self.page.go_back()
        self.page.get_by_placeholder("Enter your email").fill(f"{data['email']}")
        self.page.get_by_role("button", name="Create a free account").click()
        time.sleep(1)
        expect(self.page.locator("h2.font-bold")).to_contain_text("Create your free account")
        expect(self.page.locator("#email")).to_have_value(f"{data['email']}")

    def Faqs_section(self):
        self.page.go_back()
        second=self.page.locator("div.m_fe19b709").nth(1)
        second.click()
        second.get_by_role("link", name="Contact us").click()
        time.sleep(2)
        expect(self.page.locator("h1.font-bold")).to_contain_text("Get in touch with Clinrol")
        self.page.go_back()
        fourth = self.page.locator("div.m_fe19b709").nth(3)
        fourth.click()
        fourth.get_by_role("link", name="privacy").click()
        time.sleep(2)
        expect(self.page.locator("h1.font-bold")).to_contain_text("Privacy Policy")
        self.page.go_back()
        fourth.click()
        fourth.get_by_role("link", name="data protection").click()
        time.sleep(2)
        expect(self.page.locator("h1.font-bold")).to_contain_text("Our commitment to data security")
        self.page.go_back()
        sixth = self.page.locator("div.m_fe19b709").nth(5)
        sixth.click()
        sixth.get_by_role("link", name="Learn more").click()
        time.sleep(2)
        expect(self.page.locator(
            "//h1[normalize-space()='Simplify how you recruit and connect with patients']")).to_be_visible()
        time.sleep(2)
        self.page.go_back()
        self.page.get_by_role("link", name = "Book a quick call").click()
        time.sleep(2)
        expect(self.page.locator("h1.font-bold")).to_contain_text("Get in touch with Clinrol")

    def Journey_to_your_next_health_breakthrough_section(self):
        self.page.go_back()
        self.page.get_by_role("link", name="Partner with us").click()
        time.sleep(2)
        expect(self.page.locator("h2.font-bold")).to_contain_text("Welcome to Clinrol")
        self.page.go_back()
        card = self.page.locator("div.text-center")
        card.get_by_role("link", name="Find a clinical trial").click()
        time.sleep(2)
        expect(self.page.locator("h1.font-semibold")).to_contain_text("Find a clinical trial near you")





