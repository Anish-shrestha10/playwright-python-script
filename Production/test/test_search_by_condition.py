from playwright.sync_api import Playwright


from Production.Page.searchByCondition import SearchByCondition


def test_search_by_condition(playwright:Playwright):
    obj = SearchByCondition(playwright)
    obj.search(
        {
            "condition": "asthma",
            "age": "60",
            "location": "australia"
        })