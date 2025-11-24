from playwright.sync_api import Playwright

from Production.Page.connect_to_trial import ConnectToTrial


def test_claim_trial(playwright:Playwright):
    obj = ConnectToTrial(playwright)
    # obj.navigate(
    # {
    #     "email":"qa.patients1.1@gmail.com",
    #     "password":"Password@123",
    # })
    obj.search_trial()
    obj.QA_section()
    obj.patient_details(
        {
            "first_name": "test",
            "Last_name": "patient",
            "email": "qa.patients1.1@gmail.com",
            "phone": "9843125788",
            "month": "11",
            "day": "20",
            "year": "1980"
        })


def test_claim_trial_empty_field(playwright:Playwright):
    obj = ConnectToTrial(playwright)
    obj.search_trial()
    obj.QA_section()
    obj.patient_details(
        {
            "first_name": "",
            "Last_name": "",
            "email": "",
            "phone": "9846312578",
            "month": "11",
            "day": "20",
            "year": "1980"
        })

def test_claim_trial_invalid_data(playwright:Playwright):
    obj = ConnectToTrial(playwright)
    obj.search_trial()
    obj.QA_section()
    obj.patient_details(
        {
            "first_name": "test",
            "Last_name": "test",
            "email": "qa.patients1.m",
            "phone": "98463578",
            "month": "3",
            "day": "30",
            "year": "1988"
        })