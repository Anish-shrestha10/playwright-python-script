
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
    "condition": "lupus",
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