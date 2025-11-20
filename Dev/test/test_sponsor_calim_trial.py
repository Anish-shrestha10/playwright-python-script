from playwright.sync_api import Playwright

from Dev.Page.Sponsor_claim_trial import ClaimTrial


def test_claim_trial(playwright:Playwright):
    obj = ClaimTrial(playwright)
    obj.navigate(
        {
            "email":"qa.sponsor1.1@gmail.com",
            "password":"Password@123"
        })
    obj.search_trial(
        {
            "condition": "cancer",
        })
    obj.claim_trial_form(
        {"firstname":"zoro",
         "lastname":"smith",
         "email":"qa.sponsor1.1@gmail.com",
         "company":"probits",
        "phone":"0457896321"}
    )

def test_claim_trial_empty_field(playwright:Playwright):
    obj = ClaimTrial(playwright)
    obj.navigate(
        {
            "email":"qa.sponsor1.1@gmail.com",
            "password":"Password@123"
        })
    obj.search_trial(
        {
            "condition": "cancer",
        })
    obj.claim_trial_form(
        {"firstname":"",
         "lastname":"",
         "email":"",
         "company":"probits",
        "phone":"0457896321"}
    )

def test_claim_trial_with_site(playwright:Playwright):
    obj = ClaimTrial(playwright)
    obj.navigate(
        {
            "email":"anish@gmail.com",
            "password":"Password@123"
        })
    obj.search_trial(
        {
            "condition": "cancer",
        })
    obj.claim_trial_form(
        {"firstname":"zoro",
         "lastname":"smith",
         "email":"qa.sponsor1.1@gmail.com",
         "company":"probits",
        "phone":"0457896321"}
    )