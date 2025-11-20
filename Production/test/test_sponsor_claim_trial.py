from playwright.sync_api import Playwright

from Production.Page.Sponsor_claim_trial import ClaimTrial



def test_claim_trial(playwright:Playwright):
    obj = ClaimTrial(playwright)
    obj.navigate(
        {
            "email": "robin@gmail.com",
            "password": "Password@123"
        })
    obj.search_trial(
        {
            "condition": "lupus",
        })
    obj.claim_trial_form(
        {"firstname": "zoro",
         "lastname": "smith",
         "email": "robin@gmail.com",
         "company": "probits",
         "phone": "0457896321"}
    )

def test_claim_trial_empty(playwright:Playwright):
    obj = ClaimTrial(playwright)
    obj.navigate(
        {
            "email": "robin@gmail.com",
            "password": "Password@123"
        })
    obj.search_trial(
        {
            "condition": "cancer",
        })
    obj.claim_trial_form(
        {"firstname": "",
         "lastname": "",
         "email": "robin@gmail.com",
         "company": "probits",
         "phone": "0457896321"}
    )

def test_claim_trial_invalid(playwright:Playwright):
    obj = ClaimTrial(playwright)
    obj.navigate(
        {
            "email": "robin@gmail.com",
            "password": "Password@123"
        })
    obj.search_trial(
        {
            "condition": "cancer",
        })
    obj.claim_trial_form(
        {"firstname": "/*-",
         "lastname": "/-",
         "email": "robin@gm/",
         "company": "probits",
         "phone": "0457896321"}
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