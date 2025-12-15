from playwright.sync_api import Playwright


from Dev.Page.searchByAI import SearchByAI


def test_search_by_AI(playwright:Playwright):
    obj = SearchByAI(playwright)
    obj.search(
        {
            "search":"COPD related trial for 20 years old in Sydney"
        })

def test_search_by_AI_condition(playwright:Playwright):
    obj = SearchByAI(playwright)
    obj.search(
        {
            "search":"heart failure"
        })

def test_search_by_AI_age(playwright:Playwright):
    obj = SearchByAI(playwright)
    obj.search(
        {
            "search":"55 years old"
        })

def test_search_by_AI_location(playwright:Playwright):
    obj = SearchByAI(playwright)
    obj.search(
        {
            "search":"Sydney"
        })