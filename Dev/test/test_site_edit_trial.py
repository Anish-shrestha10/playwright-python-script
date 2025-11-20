from playwright.sync_api import Playwright

from Dev.Page.site_edit_trial import editTrial


def test_site_trial(playwright:Playwright):
    obj = editTrial(playwright)
    obj.navigate(
        {
            "email":"anish@gmail.com",
            "password":"Password@123"
        })
    obj.edit_trial(
        {
        "start_date": "2025-09-26",
        "end_date" : "2025-10-13",
        "target" : "500",
        "inclusive_question" : "inclusion",
        "exclusion_question" : "exclusion",
        "trial":"SGLT2"
        })