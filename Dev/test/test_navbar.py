from playwright.async_api import Playwright

from Dev.Page.navbar import Navbar


def test_navbar(playwright:Playwright):
    obj = Navbar(playwright)
    obj.check_navbar()