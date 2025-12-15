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
            "country_code":"Nepal (+977)",
            "phone_number":"9843125788",
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
            "location": "Location: 1110 (Research Site)",
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
