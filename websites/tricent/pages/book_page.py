from base.commands import Browser_commands
from base.urls import *
from base.selectors import *
import pytest


@pytest.fixture(scope="class",autouse=True)
def driver():
    try:
        driver = Browser_commands(Urls.tricentis_url)
        yield driver
        driver.closing_browser()
    except:
        print("driver not found.Something went wrong in driver!!")


@pytest.fixture(autouse=True)
def go_to_main_page(driver):
    try:
        driver.new_webpage(Urls.tricentis_url)
    except:
        print("Something went wrong in opening website")

@pytest.fixture
def book(driver):
    try:
        driver.click_on_element_CSS(tricent_selectors.tricentHeader_books)
    except:
        print("Something wrong in book selector")
