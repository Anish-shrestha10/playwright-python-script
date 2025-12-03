import time


from playwright.sync_api import Playwright,expect


class Profile:
    def __init__(self,playwright:Playwright):
        self.browser = playwright.chromium.launch(headless=False)
        self.page = self.browser.new_page()
        self.page.goto("https://www.clinrol.com/")


    def navigate(self,data):
        self.page.get_by_role("button", name="Log in").click()
        self.page.locator("#email").fill(data['email'])
        self.page.locator("#password").fill(data['password'])
        self.page.get_by_role("button", name="Continue").click()
        # self.page.get_by_role("link", name="Dashboard").click()
        time.sleep(3)
        self.page.get_by_role("link", name="Profile").first.click()

    def update_personal_information(self,personal_information_data):

         # personal information
         self.page.locator("#first-name").fill(personal_information_data['first_name'])
         self.page.locator("#last-name").fill(personal_information_data['last_name'])
         # self.page.locator("#email-address").fill(personal_information_data['email'])

         self.page.locator("//button[@aria-label='Select Country Code']//*[name()='svg']").click()
         self.page.locator("//button[normalize-space()='Nepal (+977)']").click()
         time.sleep(3)
         self.page.get_by_placeholder("Enter your phone number").fill(personal_information_data['phone'])
         self.page.locator("#organization_name").fill(personal_information_data['organization'])

    def update_address(self, Address_data):
        # address
        self.page.locator("#street-address").fill(Address_data['street_address'])
        self.page.locator("#city").fill(Address_data['city'])
        self.page.locator("#state").fill(Address_data['state'])
        self.page.locator("#country").fill(Address_data['country'])
        self.page.locator("#zip-code").fill(Address_data['zip_code'])



    def update_time_zone(self):
        combobox_button = self.page.locator("//button[@role='combobox']")
        text = combobox_button.text_content()
        print(text)
        combobox_button.click()
        if "Asia/Kathmandu" in text:
            self.page.get_by_placeholder("Search timezone...").fill("Australia/Sydney")
        else:
            self.page.get_by_placeholder("Search timezone...").fill("Asia/Kathmandu")
        # Wait for dropdown items to appear and click the right one
        dropdown_item = self.page.locator("div.items-center.rounded-sm")
        dropdown_item.wait_for(state="visible")
        dropdown_item.click()
        # Wait for Save button to be enabled and click
        save_button = self.page.get_by_role("button", name="Save changes")
        save_button.click()
        # Wait for toast notification, check for success
        toast = self.page.locator(".Toastify__toast")
        # expect(toast).to_contain_text("Profile updated successfully")

        response = self.page.locator(".Toastify__toast").text_content()
        if response == "Profile updated successfully":
            print(f"Test passed : {response}")
        else:
            print(f"Test failed : {response}")
        # Short wait for UI update (optional, use only if UI flickers)
        time.sleep(1)