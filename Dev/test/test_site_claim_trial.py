from playwright.sync_api import Playwright

from Dev.Page.site_claim_trial import ClaimTrial


def test_claim_trial(playwright:Playwright):
    obj = ClaimTrial(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123"
        })
    obj.search_trial(
        {
            "condition":"heart failure"
        })
    obj.claim_trial_form(
        {"firstname":"law",
         "lastname":"stha",
         "email":"qa.site1.1@gmail.com",
         "company":"probit",
        "phone":"9843125788"}
    )
def test_claim_trial_without_login(playwright:Playwright):
    obj = ClaimTrial(playwright)
    obj.search_trial(
        {
            "condition":"depression"
        })
    obj.claim_trial_form(
        {"firstname":"law",
         "lastname":"stha",
         "email":"anish@gmail.com",
         "company":"probit",
        "phone":"9843125788"}
    )

def test_claim_trial_empty_fields(playwright:Playwright):
    obj = ClaimTrial(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123"
        })
    obj.search_trial(
        {
            "condition": "cancer"
        })
    obj.claim_trial_form(
        {"firstname":"",
         "lastname":"",
         "email":"qa.site1.1@gmail.com",
         "company":"probits",
        "phone":"9843125788"}
    )
def test_claim_trial_invalid_data(playwright:Playwright):
    obj = ClaimTrial(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123"
        })
    obj.search_trial(
        {
            "condition": "cancer"
        })
    obj.claim_trial_form(
        {"firstname":"law",
         "lastname":"stha",
         "email":"qa.site1.1@gmai",
         "company":"probit",
        "phone":"9843125788"}
    )

def test_claim_trial_with_sponsor_login(playwright:Playwright):
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
         "email":"qa.site1.1@gmail.com",
         "company":"probits",
        "phone":"9843125788"}
    )