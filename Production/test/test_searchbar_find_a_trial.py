
from playwright.sync_api import Playwright

from Production.Page.searchbar_find_a_trial import SearchBar


def test_claim_trial(playwright:Playwright):
    obj = SearchBar(playwright)
    # obj.navigate()
    obj.search({
    "condition": "cancer",
    "place": "Australia",
    "age":"55"
  })