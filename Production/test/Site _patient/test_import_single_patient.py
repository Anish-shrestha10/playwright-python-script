from playwright.sync_api import Playwright

from Production.Page.Site_patient.Import_single_patient import ImportSinglePatient


def test_import_single_patient(playwright:Playwright):
    obj = ImportSinglePatient(playwright)
    obj.navigate(
        {
            "email": "qa.site1.1@gmail.com",
            "password": "Password@123"
        })
    obj.import_single_patient(
        {
            "location":"Location: 1 (Washington University in St. Louis)",
            "country_code":"Australia (+61)",
            "phone_number":"468098739",
            "first_name":"test",
            "last_name":"import",
            "email":"qa.patients1.1@gmail.com",
            "date":"2025-12-05",
            "gender":"Male",
            "ethnicity":"South Asian",
            "zip_code":"3125"
        })

def test_import_single_patient_empty(playwright: Playwright):
    obj = ImportSinglePatient(playwright)
    obj.navigate(
        {
            "email": "qa.site1.1@gmail.com",
            "password": "Password@123"
        })
    obj.import_single_patient(
        {
            "location": "Location: 1 (Washington University in St. Louis)",
            "country_code": "Nepal (+977)",
            "phone_number": "",
            "first_name": "",
            "last_name": "",
            "email": "",
            "date": "",
            "gender": "Male",
            "ethnicity": "South Asian",
            "zip_code": ""
        })

def test_import_single_patient_invalid_email(playwright: Playwright):
    obj = ImportSinglePatient(playwright)
    obj.navigate(
        {
            "email": "qa.site1.1@gmail.com",
            "password": "Password@123"
        })
    obj.import_single_patient(
        {
            "location": "Location: 1 (Washington University in St. Louis)",
            "country_code": "Nepal (+977)",
            "phone_number": "9843125788",
            "first_name": "test",
            "last_name": "test",
            "email": "qa.patients1.1@gma",
            "date": "2025-12-05",
            "gender": "Male",
            "ethnicity": "South Asian",
            "zip_code": "3125"
        })