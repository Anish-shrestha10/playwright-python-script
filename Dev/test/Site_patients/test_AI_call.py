from playwright.sync_api import Playwright

from Dev.Page.Site_patient.AI_call import AiCall


def test_ai_call(playwright:Playwright):
    obj = AiCall(playwright)
    obj.navigate(
        {
            "email":"anish@gmail.com",
            "password":"Password@123"
        })
    obj.ai_call_patient()