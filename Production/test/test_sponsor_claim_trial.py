from playwright.sync_api import Playwright

from Production.Page.Sponsor_claim_trial import ClaimTrial



def test_claim_trial(playwright:Playwright):
    obj = ClaimTrial(playwright)
    obj.navigate(
        {
            "email": "qa.sponsor1.1@gmail.com",
            "password": "Password@123"
        })
    obj.search_trial(
        {
            "condition": "lupus",
        })
    obj.claim_trial_form(
        {"firstname": "sanji",
         "lastname": "smith",
         "email": "robin@gmail.com",
         "company": "probits",
         "phone": "0457896321",
         "country_code":"Australia (+61)"}
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
        "phone":"0457896321",
         "country_code":"Australia (+61)"}
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
         "company": "Probits",
         "phone": "0457632154",
         "country_code":"Australia (+61)"}
    )

def test_claim_trial_invalid_email(playwright:Playwright):
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
        {"firstname": "robin",
         "lastname": "robin",
         "email": "robin@gmm",
         "company": "probits",
         "phone": "0457896321",
         "country_code":"Australia (+61)"}
    )

def test_claim_trial_with_site(playwright:Playwright):
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
        "phone":"0457896321",
         "country_code":"Australia (+61)"}
    )