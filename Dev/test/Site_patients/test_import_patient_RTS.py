from playwright.sync_api import Playwright

from Dev.Page.Site_patient.Import_patient_RTS import ImportPatientRTS



def test_import_single_patient(playwright:Playwright):
    obj = ImportPatientRTS(playwright)
    obj.navigate(
        {
            "email": "qa.site1.1@gmail.com",
            "password": "Password@123"
        })
    obj.import_patient_RTS(
        {
            "location": "Location: 1539 (The George Institute for Global Health)"
        })
