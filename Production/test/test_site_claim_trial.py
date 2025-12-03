from playwright.sync_api import Playwright

from Production.Page.site_claim_trial import ClaimTrial


def test_claim_trial(playwright:Playwright):
    obj = ClaimTrial(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123"
        })
    obj.search_trial(
        {
            "condition":"COPD"
        })
    obj.claim_trial_form(
        {"firstname":"anish",
         "lastname":"shrestha",
         "email":"qa.site1.1@gmail.com",
         "company":"probits",
        "phone":"9843125788",
         "country_code":"Nepal (+977)",
         "issue": "claim requested"
         }
    )

def test_claim_trial_without_login(playwright:Playwright):
    obj = ClaimTrial(playwright)
    obj.search_trial(
        {
            "condition":"COPD"
        })
    obj.claim_trial_form(
        {"firstname":"anish",
         "lastname":"shrestha",
         "email":"nami@gmail.com",
         "company":"probits",
        "phone":"9843125788",
         "country_code":"Nepal (+977)",
         "issue":"User have to login in"}
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
        "phone":"9843125788",
         "country_code":"Nepal (+977)",
         "issue":"empty fields"
         }
    )

def test_claim_trial_invalid_email(playwright:Playwright):
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
        {"firstname":"nami",
         "lastname":"anime",
         "email":"nami@gma",
         "company":"probits",
        "phone":"9843125788",
         "country_code":"Nepal (+977)",
         "issue":"invalid credentials"
         }
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
        "phone":"9843125788",
         "country_code":"Nepal (+977)",
         "issue":"site user should login to claim as site"
         }
    )