from playwright.sync_api import Playwright

from Dev.Page.edit_pre_screening import editPreScreening


def test_site_trial(playwright:Playwright):
    obj = editPreScreening(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123"
        })
    obj.edit_pre_screening(
        {
            "trial": "Computed Tomography Coronary Angiography for the Prevention of Myocardial Infarction (The SCOT-HEART 2 Trial)"
        })