from playwright.sync_api import Playwright

from Dev.Page.filterByDisease import FilterByCondition


def test_claim_trial(playwright:Playwright):
    obj = FilterByCondition(playwright)
    obj.navigate()
    obj.filter(
        {
            "disease":"COPD"
        })