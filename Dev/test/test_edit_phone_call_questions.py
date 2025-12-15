from playwright.sync_api import Playwright

from Dev.Page.edit_phone_call_questions import editPhoneCall


def test_site_trial(playwright:Playwright):
    obj = editPhoneCall(playwright)
    obj.navigate(
        {
            "email": "qa.site1.1@gmail.com",
            "password": "Password@123"
        })
    obj.edit_phone_call(
        {
            "trial": "Computed Tomography Coronary Angiography for the Prevention of Myocardial Infarction (The SCOT-HEART 2 Trial)"
        })
