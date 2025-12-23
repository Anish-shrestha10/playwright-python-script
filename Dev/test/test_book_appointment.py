from datetime import date

from playwright.sync_api import Playwright

from Dev.Page.Book_appointment import Appointment

today = date.today()
def test_book_appointment_AI_call(playwright:Playwright):
    obj = Appointment(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123",
        })
    obj.book_appointment(
        {
            "title":"AI call",
            "type":"AI Call",
            "date":f"{today}",
            "hour":"12",
            "minute":"00",
            "am/pm":"AM",
            "duration":"30 minutes",
            "priority":"Low",
            "patient":"tester testing"
        })

def test_book_appointment_visit(playwright:Playwright):
    obj = Appointment(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123",
        })
    obj.book_appointment(
        {
            "title":"Visit",
            "type":"Visit",
            "date":f"{today}",
            "hour":"1",
            "minute":"00",
            "am/pm":"PM",
            "duration":"60 minutes",
            "priority":"Low",
            "patient":"tester testing"
        })

def test_book_appointment_phone_call(playwright:Playwright):
    obj = Appointment(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123",
        })
    obj.book_appointment(
        {
            "title":"Phone Call",
            "type":"Phone Call",
            "date":f"{today}",
            "hour":"10",
            "minute":"00",
            "am/pm":"AM",
            "duration":"45 minutes",
            "priority":"Low",
            "patient":"tester testing"
        })

def test_book_appointment_custom_event(playwright:Playwright):
    obj = Appointment(playwright)
    obj.navigate(
        {
            "email":"qa.site1.1@gmail.com",
            "password":"Password@123",
        })
    obj.book_appointment(
        {
            "title":"Custom Event",
            "type":"Custom Event",
            "date":f"{today}",
            "hour":"11",
            "minute":"00",
            "am/pm":"AM",
            "duration":"15 minutes",
            "priority":"Low",
            "patient":"tester testing"
        })