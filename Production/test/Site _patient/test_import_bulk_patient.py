from playwright.sync_api import Playwright

from Production.Page.Site_patient.Import_bulk_patient import ImportBulkPatient



def test_import_single_patient(playwright:Playwright):
    obj = ImportBulkPatient(playwright)
    obj.navigate(
        {
            "email": "qa.site1.1@gmail.com",
            "password": "Password@123"
        })
    obj.import_bulk_patient()
