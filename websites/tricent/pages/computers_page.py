from base.commands import Browser_commands
from base.urls import *
from base.selectors import *
import pytest
from time import sleep


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
def computers_desktop(driver):
    try:
        driver.hover_CSS(tricent_selectors.tricentHeader_comuters)
        # driver.hover_CSS(element)
        # element.cl
        driver.click_on_element_CSS("body > div.master-wrapper-page > div.master-wrapper-content > div.header-menu > ul.top-menu > li:nth-child(2) > ul > li:nth-child(1) > a")
        sleep(1)
        # sleep(1)
    except:
        print("Something wrong in computers selector")