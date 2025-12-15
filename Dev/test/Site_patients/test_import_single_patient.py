from playwright.sync_api import Playwright

from Dev.Page.Site_patient.Import_single_patient import ImportSinglePatient
from datetime import date


def test_import_single_patient(playwright:Playwright):
    obj = ImportSinglePatient(playwright)
    obj.navigate(
        {
            "email": "qa.site1.1@gmail.com",
            "password": "Password@123"
        })
    obj.import_single_patient(
        {
            "location":"Location: 1539 (The George Institute for Global Health)",
            "country_code":"Australia (+61)",
            "phone_number":"468098739",
            "first_name":"Probits",
            "last_name":"testing",
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
            "location": "Location: 1539 (The George Institute for Global Health)",
            "country_code": "Nepal (+977)",
            "phone_number": "9843125788",
            "first_name": "",
            "last_name": "",
            "email": "qa.patients1.1@gmail.com",
            "date": "2025-12-05",
            "gender": "",
            "ethnicity": "South Asian",
            "zip_code": "3125"
        })
