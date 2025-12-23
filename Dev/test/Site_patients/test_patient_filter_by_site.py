from playwright.sync_api import Playwright

from Dev.Page.Site_patient.patient_filter_by_site import filterBySite


def test_patient_filter_by_site(playwright:Playwright):
    obj = filterBySite(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123"
        })
    obj.filter_by_site(
        {
            "site": "MetroHealth Medical Center"
        })