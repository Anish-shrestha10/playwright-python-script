from playwright.sync_api import Playwright


from Dev.Page.searchByCondition import SearchByCondition


def test_search_by_condition(playwright:Playwright):
    obj = SearchByCondition(playwright)
    obj.search(
        {
            "condition":"lupus",
            "age":"60",
            "location":"australia"
        })

def test_search_by_condition_conditionOnly(playwright:Playwright):
    obj = SearchByCondition(playwright)
    obj.search(
        {
            "condition":"lupus",
            "age":"",
            "location":""
        })

def test_search_by_condition_ageOnly(playwright:Playwright):
    obj = SearchByCondition(playwright)
    obj.search(
        {
            "condition":"",
            "age":"60",
            "location":""
        })

def test_search_by_condition_locationOnly(playwright:Playwright):
    obj = SearchByCondition(playwright)
    obj.search(
        {
            "condition":"",
            "age":"",
            "location":"australia"
        })