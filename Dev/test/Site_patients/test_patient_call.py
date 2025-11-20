from playwright.sync_api import Playwright

from Dev.Page.Site_patient.Patient_call import callPatient


def test_patient_call(playwright:Playwright):
    obj = callPatient(playwright)
    obj.navigate(
        {
            "email":"anish@gmail.com",
            "password":"Password@123"
        })
    obj.call_patient()