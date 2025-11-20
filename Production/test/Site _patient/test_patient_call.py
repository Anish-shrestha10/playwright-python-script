from playwright.sync_api import Playwright

from Production.Page.Site_patient.Patient_call import callPatient


def test_patient_call(playwright:Playwright):
    obj = callPatient(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123"
        })
    obj.call_patient()