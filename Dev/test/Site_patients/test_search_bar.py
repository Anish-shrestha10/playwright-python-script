from playwright.sync_api import Playwright

from Dev.Page.Site_patient.search_bar import search_bar


def test_search_bar(playwright:Playwright):
    obj = search_bar(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123",
        })
    obj.search(
        {
            "patient_name":"testing"
        })
