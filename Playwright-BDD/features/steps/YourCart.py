from behave import *
from playwright.sync_api import expect

@then("click on checkout")
def click_checkout(context):
    context.page.get_by_role("button", name="Checkout").click()
    context.page.close()