from behave import *
from playwright.sync_api import expect


@given("username and password")
def fill_username_and_password(context):
    context.page.goto("https://www.saucedemo.com/")

    context.page.get_by_role("textbox", name="Username").fill("standard_user")
    context.page.get_by_role("textbox", name="Password").fill("secret_sauce")
    


@when("Log In button clicked")
def click_login(context):
    context.page.get_by_role(
        "button", name="Login"
    ).click()


