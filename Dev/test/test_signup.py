from playwright.sync_api import Playwright

from Dev.Page.Signup import Signup


def test_valid_data(playwright:Playwright):
    obj = Signup(playwright)
    obj.navigate()
    obj.signup({
    "first_name": "Site",
    "last_name": "Shrestha",
    "email": "qa.site1.1+32@gmail.com",
    "selectOption": "Site",
    "Organization": "probits",
    "password": "Password@123",
    "confirmPassword":  "Password@123"
    })

def test_same_email(playwright: Playwright):
    obj = Signup(playwright)
    obj.navigate()
    obj.signup({
      "first_name": "Patient",
    "last_name": "Shrestha",
    "email": "qa.site1.1@gmail.com",
    "selectOption": "Site",
    "Organization": "probits",
    "password": "Password@123",
    "confirmPassword":  "Password@123"
    })

def test_invalid_data(playwright: Playwright):
    obj = Signup(playwright)
    obj.navigate()
    obj.signup({
      "first_name": "/*-+",
    "last_name": "/*-+",
    "email": "patient881@gmail.com",
    "selectOption": "Sponsor",
      "Organization": "/*-+",
    "password": "Password@123",
    "confirmPassword":  "Password@123"
    })


def test_invalid_email(playwright: Playwright):
    obj = Signup(playwright)
    obj.navigate()
    obj.signup({
        "first_name": "Patient",
        "last_name": "Patients",
        "email": "patient52@gmaom",
        "selectOption": "Site",
        "Organization": "probits",
        "password": "Password@123",
        "confirmPassword": "Password@123"
    })

def test_mismatched_password(playwright: Playwright):
    obj = Signup(playwright)
    obj.navigate()
    obj.signup({
        "first_name": "Patient",
        "last_name": "Patients",
        "email": "patient52@gmail.com",
        "selectOption": "Site",
        "Organization": "probits",
        "password": "Password@123",
        "confirmPassword": "Password@1"
    })

def test_empty_data(playwright: Playwright):
    obj = Signup(playwright)
    obj.navigate()
    obj.signup({
      "first_name": "",
    "last_name": "",
    "email": "",
    "selectOption": "Patient",
      "Organization": "",
    "password": "",
    "confirmPassword":  ""
    })


