from behave import *
from playwright.sync_api import expect

@then("enter your info")
def enter_info(context):
    context.page.locator("[data-test=\"firstName\"]").fill("321321321")
    context.page.locator("[data-test=\"lastName\"]").fill("dsadsadsa")
    context.page.locator("[data-test=\"postalCode\"]").fill("cxzcxcxz")
    context.page.locator("[data-test=\"continue\"]").click()

    
