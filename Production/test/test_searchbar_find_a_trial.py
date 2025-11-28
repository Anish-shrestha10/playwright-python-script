
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

def test_searchbar_find_a_trial_age(playwright:Playwright):
    obj = SearchBar(playwright)
    obj.navigate()
    obj.search({
    "condition": "",
    "place": "",
    "age":"40"
  })

def test_searchbar_find_a_trial_condition(playwright:Playwright):
    obj = SearchBar(playwright)
    obj.navigate()
    obj.search({
    "condition": "asthma",
    "place": "",
    "age":""
  })

def test_searchbar_find_a_trial_place(playwright:Playwright):
    obj = SearchBar(playwright)
    obj.navigate()
    obj.search({
    "condition": "",
    "place": "australia",
    "age":""
  })