from behave import *
from pytest import fail
from selenium.common.exceptions import NoSuchElementException


@given('I search for "{text}"')
def step_impl(context, text):
    context.browser.get('https://www.google.ca/search?q='+text)


@then('the result page will include "{text}"')
def step_impl(context, text):
    try:
        context.browser.find_element_by_partial_link_text(text)
    except NoSuchElementException:
        fail('%r not in result page' % text)
        pass
