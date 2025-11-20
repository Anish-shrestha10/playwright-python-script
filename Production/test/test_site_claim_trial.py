from playwright.sync_api import Playwright

from Production.Page.site_claim_trial import ClaimTrial


def test_claim_trial(playwright:Playwright):
    obj = ClaimTrial(playwright)
    obj.navigate(
        {
            "email":"nami@gmail.com",
            "password":"Password@123"
        })
    obj.search_trial(
        {
            "condition":"heart"
        })
    obj.claim_trial_form(
        {"firstname":"anish",
         "lastname":"shrestha",
         "email":"nami@gmail.com",
         "company":"probits",
        "phone":"9843125788"}
    )

def test_claim_trial_empty(playwright:Playwright):
    obj = ClaimTrial(playwright)
    obj.navigate(
        {
            "email":"nami@gmail.com",
            "password":"Password@123"
        })
    obj.search_trial(
        {
            "condition":"cancer"
        })
    obj.claim_trial_form(
        {"firstname":"",
         "lastname":"",
         "email":"nami@gmail.com",
         "company":"probits",
        "phone":"9843125788"}
    )

def test_claim_trial_with_sponsor(playwright:Playwright):
    obj = ClaimTrial(playwright)
    obj.navigate(
        {
            "email":"qa.sponsor1.1@gmail.com",
            "password":"Password@123"
        })
    obj.search_trial(
        {
            "condition":"depression"
        })
    obj.claim_trial_form(
        {"firstname":"law",
         "lastname":"stha",
         "email":"anish@gmail.com",
         "company":"probits",
        "phone":"9843125788"}
    )