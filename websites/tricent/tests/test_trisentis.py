from pages.book_page import *
from pages.computers_page import *
from pages.electronics_page import *
from selenium.common.exceptions import *
from time import sleep

class Test_tricent_book:
    @pytest.mark.usefixtures("book")
    @pytest.mark.parametrize("product_index", [1, 2, 3, 4, 5, 6])
    def test_book_products(self,driver,product_index):
        try:
            driver.click_on_element_CSS(f"body > div.master-wrapper-page > div.master-wrapper-content > div.master-wrapper-main > div.center-2 > div.page.category-page > div.page-body > div.product-grid > div:nth-child({product_index}) > div > div.picture > a > img")
            sleep(1)
            assert driver.is_element_visible_CSS("#product-details-form > div > div.product-essential > div.overview > div.prices > div.product-price > span"),"the element not visible"
        except (TimeoutException,NoSuchElementException) as e:
            print("didn't found any element")


 
class Test_tricent_computers:
    @pytest.mark.usefixtures("computers_desktop")
    @pytest.mark.parametrize("product_index", [1, 2, 3, 4, 5, 6])
    def test_computers_desktop_products(self, driver,product_index):
        try:
            driver.click_on_element_CSS(f"body > div.master-wrapper-page > div.master-wrapper-content > div.master-wrapper-main > div.center-2 > div.page.category-page > div.page-body > div.product-grid > div:nth-child({product_index}) > div > div.picture > a > img")
            sleep(1)
            assert driver.is_element_visible_CSS("#product-details-form > div > div.product-essential > div.overview > div.prices > div.product-price > span"),"the element not visible"
        except (TimeoutException,NoSuchElementException) as e:
            print("didn't found any element")



class Test_tricent_electronics:
    @pytest.mark.usefixtures("electronics_camera")
    @pytest.mark.parametrize("product_index", [1, 2, 3, 4])
    def test_C1_electronics_camera(self, driver,product_index):
        try:
            driver.click_on_element_CSS(f"body > div.master-wrapper-page > div.master-wrapper-content > div.master-wrapper-main > div.center-2 > div.page.category-page > div.page-body > div.product-grid > div:nth-child({product_index}) > div > div.picture > a > img")
            sleep(1)
            assert driver.is_element_visible_CSS("#product-details-form > div > div.product-essential > div.overview > div.prices > div.product-price > span"),"the element not visible"
        except (TimeoutException,NoSuchElementException) as e :
            print("didn't found any element")
 