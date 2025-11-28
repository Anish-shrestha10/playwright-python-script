from playwright.sync_api import Playwright


from Production.Page.searchByAI import SearchByAI


def test_search_by_AI(playwright:Playwright):
    obj = SearchByAI(playwright)
    obj.search(
        {
            "prompt":"cancer related trial for 55 years old in Sydney"
        })

def test_search_by_AI_condition(playwright:Playwright):
    obj = SearchByAI(playwright)
    obj.search(
        {
            "prompt":"heart failure"
        })

def test_search_by_AI_age(playwright:Playwright):
    obj = SearchByAI(playwright)
    obj.search(
        {
            "prompt":"55 years old"
        })

def test_search_by_AI_location(playwright:Playwright):
    obj = SearchByAI(playwright)
    obj.search(
        {
            "prompt":"Sydney"
        })