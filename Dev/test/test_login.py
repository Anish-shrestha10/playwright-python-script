from playwright.sync_api import Playwright

from Dev.Page.login import Login

def test_valid_data(playwright:Playwright):
    obj = Login(playwright)
    obj.navigate()
    obj.login( {
    "user_email": "qa.site1.1@gmail.com",
    "user_password": "Password@123",
    "issue":"User logged in"
  })

def test_invalid_data(playwright:Playwright):
    obj = Login(playwright)
    obj.navigate()
    obj.login( {
    "user_email": "patient32@gmaom",
    "user_password": "Prd@123",
    "issue":"invalid credentials"
  })

def test_different_password(playwright:Playwright):
    obj = Login(playwright)
    obj.navigate()
    obj.login( {
    "user_email": "qa.site1.1@gmail.com",
    "user_password": "Prd@123",
    "issue":"invalid password"
  })

def test_empty_data(playwright:Playwright):
    obj = Login(playwright)
    obj.navigate()
    obj.login( {
    "user_email": "qa.site1.1@gmail.com",
    "user_password": "",
    "issue":"empty field"
  })

def test_forget_password(playwright:Playwright):
    obj = Login(playwright)
    obj.navigate()
    obj.forgetPassword(
        {
            "reset_email":"qa.site1.1@gmail.com",
            "issue":"reset link send"
        })

def test_forget_password_empty(playwright:Playwright):
    obj = Login(playwright)
    obj.navigate()
    obj.forgetPassword(
        {
            "reset_email":"",
            "issue":"empty email field"
        })