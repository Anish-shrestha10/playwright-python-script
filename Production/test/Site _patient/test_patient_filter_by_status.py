from playwright.sync_api import Playwright

from Production.Page.Site_patient.patient_filter_by_status import filterByStatus


def test_patient_filter_by_status(playwright:Playwright):
    obj = filterByStatus(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123"
        })
    obj.filter_by_status()