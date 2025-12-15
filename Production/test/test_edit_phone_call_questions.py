from playwright.sync_api import Playwright

from Production.Page.edit_phone_call_questions import editPhoneCall


def test_site_trial(playwright:Playwright):
    obj = editPhoneCall(playwright)
    obj.navigate(
        {
            "email": "qa.site1.1@gmail.com",
            "password": "Password@123"
        })
    obj.edit_phone_call(
        {
            "trial": "Open Label Study of Acthar SQ Gel Injection in Patients With Active Anterior Uveitis"
        })