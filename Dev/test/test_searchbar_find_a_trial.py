
from playwright.sync_api import Playwright

from Dev.Page.searchbar_find_a_trial import SearchBar


def test_searchbar_find_a_trial_1(playwright:Playwright):
    obj = SearchBar(playwright)
    obj.navigate()
    obj.search({
    "condition": "lupus",
    "place": "australia",
    "age":"55"
  })

def test_searchbar_find_a_trial_2(playwright:Playwright):
    obj = SearchBar(playwright)
    obj.navigate()
    obj.search({
    "condition": "cancer",
    "place": "sydney",
    "age":"40"
  })