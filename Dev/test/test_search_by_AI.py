from playwright.sync_api import Playwright


from Dev.Page.searchByAI import SearchByAI


def test_search_by_AI(playwright:Playwright):
    obj = SearchByAI(playwright)
    obj.search(
        {
            "search":"cancer related trial for 20 years old in Sydney"
        })