
from playwright.sync_api import Playwright
from Dev.Page.Homepage import Homepage


def test_homepage(playwright:Playwright):
    obj = Homepage(playwright)
    obj.browse_by_condition(
        {
            "condition":"Lung cancer"
        })

    obj.how_clinrol_works_section()
    obj.how_clinrol_helps_sponsors_sites()
    obj.trusted_by_over_100k_section(
        {
            "email": "anish@gmail.com",
        })
    obj.Faqs_section()
    obj.Journey_to_your_next_health_breakthrough_section()