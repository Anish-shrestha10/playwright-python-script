from playwright.sync_api import Playwright

from Production.Page.Help_form import HelpForm


def test_help(playwright:Playwright):
    obj = HelpForm(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123"
        })
    obj.form(
        {
            "fullname":"test help",
            "country_code":"Nepal (+977)",
            "number":"9843125788",
            "email":"anish@gmail.com",
            "role":"Sponsor",
            "message":"hello world"
        })

def test_invalid_data(playwright:Playwright):
    obj = HelpForm(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123"
        })
    obj.form(
        {
            "fullname":"Anish shrestha",
            "country_code":"Nepal (+977)",
            "number":"984",
            "email":"anish@gmail.com",
            "role":"Sponsor",
            "message":"hello world"
        })

def test_invalid_email(playwright:Playwright):
    obj = HelpForm(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123"
        })
    obj.form(
        {
            "fullname":"Anish shrestha",
            "country_code":"Nepal (+977)",
            "number":"98431258",
            "email":"anish@gma",
            "role":"Sponsor",
            "message":"hello world"
        })

def test_empty_field(playwright:Playwright):
    obj = HelpForm(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123"
        })
    obj.form(
        {
            "fullname":"",
            "country_code":"Nepal (+977)",
            "number":"",
            "email":"",
            "role":"Sponsor",
            "message":""
        })