from playwright.sync_api import Playwright

from Dev.Page.Site_trial import siteTrial


def test_site_trial(playwright:Playwright):
    obj = siteTrial(playwright)
    obj.navigate(
        {
            "email": "anish@gmail.com",
            "password": "Password@123"
        })
    obj.search_bar()
    obj.Active_trial()
    obj.Pending_trial()