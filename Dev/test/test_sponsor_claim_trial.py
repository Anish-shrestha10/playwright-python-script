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
            "condition": "lungs",
        })
    obj.claim_trial_form(
        {"firstname":"zoro",
         "lastname":"smith",
         "email":"qa.sponsor1.1@gmail.com",
         "company":"probits",
        "phone":"0457896321"
         }
    )

def test_claim_trial_without_login(playwright:Playwright):
    obj = ClaimTrial(playwright)
    obj.search_trial(
        {
            "condition": "cancer",
        })
    obj.claim_trial_form(
        {"firstname":"zoro",
         "lastname":"smith",
         "email":"qa.sponsor1.1@gmail.com",
         "company":"probits",
        "phone":"0457896321"
         }
    )

def test_claim_trial_invalid_data(playwright:Playwright):
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
         "lastname":"shrestha",
         "email":"anish@gma",
         "company":"probits",
        "phone":"0457896154"
         }
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
         "email":"qa.site1.1@gmail.com",
         "company":"probits",
        "phone":"0457896321"
         }
    )

def test_claim_trial_with_site_login(playwright:Playwright):
    obj = ClaimTrial(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
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