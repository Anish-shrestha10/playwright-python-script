from playwright.sync_api import Playwright

from Dev.Page.Site_patient.patient_filter_by_trail import filterByTrail


def test_patient_filter_by_trail(playwright:Playwright):
    obj = filterByTrail(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123"
        })
    obj.filter_by_trail(
        {
            "trial":"SGLT2"
        })