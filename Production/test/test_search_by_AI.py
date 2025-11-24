from playwright.sync_api import Playwright


from Production.Page.searchByAI import SearchByAI


def test_search_by_AI(playwright:Playwright):
    obj = SearchByAI(playwright)
    obj.search(
        {
            "prompt":"cancer related trial for 55 years old in Sydney"
        })