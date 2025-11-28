from playwright.sync_api import Playwright

from Dev.Page.edit_AI_call_question import editAICallQuestion


def test_site_trial(playwright:Playwright):
    obj = editAICallQuestion(playwright)
    obj.navigate(
        {
            "email": "qa.site1.1@gmail.com",
            "password": "Password@123"
        })
    obj.edit_AI_call_question(
        {
            "trial":"Computed Tomography Coronary Angiography for the Prevention of Myocardial Infarction (The SCOT-HEART 2 Trial)"
        })