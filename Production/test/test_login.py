from playwright.sync_api import Playwright

from Production.Page.login import Login

def test_valid_data(playwright:Playwright):
    obj = Login(playwright)
    obj.navigate()
    obj.login( {
    "user_email": "qa.site1.1@gmail.com",
    "user_password": "Password@123"
  })

def test_invalid_data(playwright:Playwright):
    obj = Login(playwright)
    obj.navigate()
    obj.login( {
    "user_email": "patient32@gmaom",
    "user_password": "Prd@123"
  })

def test_empty_data(playwright:Playwright):
    obj = Login(playwright)
    obj.navigate()
    obj.login( {
    "user_email": "qa.site1.1@gmail.com",
    "user_password": ""
  })

def test_forget_password(playwright:Playwright):
    obj = Login(playwright)
    obj.navigate()
    obj.forgetPassword()