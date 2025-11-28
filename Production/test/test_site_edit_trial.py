from playwright.sync_api import Playwright

from Production.Page.site_edit_trial import editTrial


def test_site_trial(playwright:Playwright):
    obj = editTrial(playwright)
    obj.navigate(
        {
            "email": "qa.site1.1@gmail.com",
            "password": "Password@123"
        })
    obj.edit_trial(
        {
        "start_date": "2025-09-28",
        "end_date" : "2026-11-16",
        "target" : "500",
        "inclusive_question" : "inclusion",
        "exclusion_question" : "exclusion",
        "trial":"Open Label Study of Acthar SQ Gel Injection in Patients With Active Anterior Uveitis"
        })

def test_empty_data(playwright:Playwright):
    obj = editTrial(playwright)
    obj.navigate(
        {
            "email": "qa.site1.1@gmail.com",
            "password": "Password@123"
        })
    obj.edit_trial(
        {
        "start_date": "",
        "end_date" : "",
        "target" : "",
        "inclusive_question" : "inclusion",
        "exclusion_question" : "exclusion",
        "trial": "Open Label Study of Acthar SQ Gel Injection in Patients With Active Anterior Uveitis"
        })