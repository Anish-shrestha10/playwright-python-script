from playwright.sync_api import Playwright

from Production.Page.Site_patient.AI_call import AiCall


def test_ai_call(playwright:Playwright):
    obj = AiCall(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123"
        })
    obj.ai_call_patient()

def test_schedule_ai_call(playwright:Playwright):
    obj = AiCall(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123"
        })
    obj.ai_call_schedule(
        {
            "date":"2025-11-27",
            "hr":"10",
            "min":"30",
            "am/pm":"AM"
        })