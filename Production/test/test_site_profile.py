from playwright.sync_api import Playwright

from Production.Page.Site_profile import Profile

def test_site_profile(playwright:Playwright):
    obj = Profile(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123",
        })
    obj.update_personal_information({
      "first_name": "Site",
      "last_name": "User",
      "phone": "9843125788",
      "organization": "probits"
    })

    obj.update_address(
        {"street_address": "Syndal, Glen Waverley VIC 3150",
      "country": "Australia",
      "city": "Glen Waverley",
      "zip_code": "3150",
      "state": "VIC"
    })

    obj.update_time_zone()

def test_site_profile_empty(playwright:Playwright):
    obj = Profile(playwright)
    obj.navigate(
        {
            "email": "robin@gmail.com",
            "password": "Password@123",
        })
    obj.update_personal_information({
      "first_name": "",
      "last_name": "",
      "phone": "",
      "organization": ""
    })

    obj.update_address(
        {"street_address": "Syndal, Glen Waverley VIC 3150",
      "country": "",
      "city": "Glen Waverley",
      "zip_code": "3150",
      "state": ""
    })

    obj.update_time_zone()