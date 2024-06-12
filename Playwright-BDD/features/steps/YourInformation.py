from behave import *
from playwright.sync_api import expect

@then("enter your info")
def enter_info(context):
    context.page.get_by_role("textbox", name="First Name").fill("Juan")
    context.page.get_by_role("textbox", name="Last Name").fill("Noname")
    context.page.get_by_role("textbox", name="Zip/Postal Code").fill("97312")
    context.page.get_by_role("textbox", name="Continue").click()
