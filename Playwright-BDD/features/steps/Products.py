from behave import *
from playwright.sync_api import expect

@then("select some products")
def select_products(context):
    context.page.locator("[data-test=\"add-to-cart-sauce-labs-backpack\"]").click()
    context.page.locator("[data-test=\"add-to-cart-sauce-labs-bike-light\"]").click()
    context.page.locator("[data-test=\"add-to-cart-sauce-labs-bolt-t-shirt\"]").click()

@then("go to shopping cart")
def Go_to_shopping_cart(context):    
    context.page.locator("[data-test=\"shopping-cart-link\"]").click()