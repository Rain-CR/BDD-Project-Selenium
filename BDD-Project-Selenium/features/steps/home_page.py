from time import sleep
from behave import *


@given("I am on the home page")
def step_impl(context):
    context.browser.driver.get("https://the-internet.herokuapp.com/")
    sleep(1)


@when("I click the link for Add/Remove Elements")
def step_impl(context):
    add_remove_elements = context.browser.get_add_remove_link()
    add_remove_elements.click()
