from playwright.sync_api import Playwright

from Dev.Page.site_overview import SiteOverview


def test_site_overview(playwright:Playwright):
    obj = SiteOverview(playwright)
    obj.navigate()
    obj.patient_view_all()
    obj.trials_view_all()
    obj.patient_details()
    obj.edit_trial()