from playwright.sync_api import Playwright

from Dev.Page.Site_patient.AI_call import AiCall
from datetime import date

today = date.today()
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
            "date":f"{today}",
            "hr":"10",
            "min":"00",
            "am/pm":"AM",
            "issue":"AI call scheduled"
        })

def test_schedule_ai_call_past_time(playwright:Playwright):
    obj = AiCall(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123"
        })
    obj.ai_call_schedule(
        {
            "date":"2025-12-02",
            "hr":"9",
            "min":"00",
            "am/pm":"AM",
            "issue":"AI call scheduled in past time"
        })