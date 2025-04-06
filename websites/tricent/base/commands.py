from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import requests
import json


class Browser_commands:
    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.driver.get(f"{url}")
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.action = ActionChains(self.driver)
        self.alert = Alert(self.driver)
        self.r = requests
        self.driver.implicitly_wait(10)

    # With CSS_SELECTOR working
    def click_on_element_CSS(self, css_selector):
        self.is_element_visible_CSS(css_selector)
        return self.is_clickable_CSS(css_selector).click()

    def hover_CSS(self, css_selector):
        element = self.is_element_visible_CSS(f"{css_selector}")
        return self.action.move_to_element(element).perform()

    def right_click_CSS(self,css_selector):
        element = self.is_element_visible_CSS(f"{css_selector}")
        return self.action.context_click(element).perform()

    def drag_drop_CSS(self,css_selector_down,css_selector_up):
        element1 = self.is_element_visible_CSS(f"{css_selector_down}")
        element2 = self.is_element_visible_CSS(f"{css_selector_up}")
        return self.action.drag_and_drop(element1,element2).perform()

    def switching_alert(self):
        return self.driver.switch_to.alert

    def alert_accept(self):
        return self.alert.accept()

    def alert_dismiss(self):
        return self.alert.dismiss()

    def alert_sendKeys(self,text):
        return self.alert.send_keys(f"{text}")

    def send_keys_CSS(self, css_selector, text):
        return self.is_element_visible_CSS(css_selector).send_keys(f"{text}")

    def enter(self):
        return self.action.send_keys(Keys.ENTER).perform()

    def clearing_CSS(self, css_selector):
        element = self.is_element_visible_CSS(css_selector)
        return element.clear()

    def get_text_CSS(self, css_selector):
        return self.is_element_visible_CSS(f"{css_selector}").text

    def get_attribute_CSS(self, css_selector, attribute_name):
        return self.is_element_present_in_DOM_CSS(f"{css_selector}").get_attribute(f"{attribute_name}")

    def is_clickable_CSS(self, css_selector):
        return self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, f"{css_selector}")))

    def is_value_present_in_attribute_CSS(self, css_selector, attribute, text):
        return self.wait.until(
            EC.text_to_be_present_in_element_attribute((By.CSS_SELECTOR, f"{css_selector}"), f"{attribute}", f"{text}"))

    def is_element_present_in_DOM_CSS(self, css_selector):
        return self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, f"{css_selector}")))

    def is_element_visible_CSS(self, css_selector):
        return self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"{css_selector}")))

    def finding_elements_CSS(self, css_selector, index):
        elements = self.driver.find_elements(By.CSS_SELECTOR, f"{css_selector}")
        return elements[index]

    def list_of_elements_CSS(self, css_selector):
        elements = self.driver.find_elements(By.CSS_SELECTOR, f"{css_selector}")
        return elements

    def finding_elements_len_CSS(self, css_selector):
        elements = self.driver.find_elements(By.CSS_SELECTOR, f"{css_selector}")
        return len(elements)

    def finding_elements_text_CSS(self, css_selector, index):
        elements = self.driver.find_elements(By.CSS_SELECTOR, f"{css_selector}")
        return elements[index].text

    def finding_elements_attribute_CSS(self, css_selector, index, attribute):
        elements = self.driver.find_elements(By.CSS_SELECTOR, f"{css_selector}")
        return elements[index].get_attribute(f"{attribute}")

    def click_on_each_element_CSS(self, css_selector):
        element = self.driver.find_elements(By.CSS_SELECTOR, f"{css_selector}")
        for each_element in element:
            each_element.click()

    def getting_text_each_element_CSS(self, css_selector):
        elements = self.driver.find_elements(By.CSS_SELECTOR, f"{css_selector}")
        for each_element in elements:
            print(each_element.text)

    def getting_attribute_each_element_CSS(self, css_selector, attribute):
        elements_list = []
        elements = self.driver.find_elements(By.CSS_SELECTOR, f"{css_selector}")
        for each_element in elements:
            elements_list.append(each_element.get_attribute(f"{attribute}"))
        return elements_list

    def switching_to_iframe_CSS(self, css_selector):
        return self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, f"{css_selector}")))

    def switch_to_the_iframe_by_index(self, index):
        return self.driver.switch_to.frame(index)

    def switching_window(self, index):
        return self.driver.switch_to.window(self.driver.window_handles[index])

    def window_handles(self, new_url):
        return self.driver.execute_script(f"window.open('{new_url}');")

    def save_screenshot(self, file_name):
        return self.driver.save_screenshot(f"reports/{file_name}.png")

    def getting_title(self):
        return self.driver.title

    def getting_url(self):
        return self.driver.current_url

    def getting_page_source(self):
        return self.driver.page_source

    def scroll(self, x, y):
        return self.driver.execute_script(f"window.scrollBy({x}, {y})")

    def checking_title(self, title):
        assert self.driver.title == f"{title}", "title didn't matched"

    def refreshPage(self):
        return self.driver.refresh()

    # Working with XPTATH

    def click_XPATH(self, xpath_selector):
        self.is_element_visible_XPATH(xpath_selector)
        return self.is_clickable_XPATH(xpath_selector).click()

    def hover_XPATH(self, xpath_selector):
        element = self.is_element_visible_XPATH(f"{xpath_selector}")
        return self.action.move_to_element(element).perform()

    def right_click_XPATH(self,xpath_selector):
        element = self.is_element_visible_XPATH(f"{xpath_selector}")
        return self.action.move_to_element(element).context_click()

    def drag_drop_XPATH(self,xpath_selector_down,xpath_selector_up):
        element1 = self.is_element_visible_CSS(f"{xpath_selector_down}")
        element2 = self.is_element_visible_CSS(f"{xpath_selector_up}")
        return self.action.drag_and_drop(element1,element2).perform()

    def send_keys_XPATH(self, xpath_selector, text):
        return self.is_element_visible_XPATH(xpath_selector).send_keys(f"{text}")

    def enter_XPATH(self, xpath_selector):
        return self.is_element_visible_XPATH(xpath_selector).send_keys(Keys.ENTER)

    def clearing_XPATH(self, xpath_selector):
        element = self.is_element_visible_XPATH(xpath_selector)
        return element.clear()

    def get_text_XPATH(self, xpath_selector):
        return self.is_element_visible_XPATH(f"{xpath_selector}").text

    def get_attribute_of_element_XPATH(self, xpath_selector, attribute_name):
        return self.is_element_present_in_DOM_XPATH(f"{xpath_selector}").get_attribute(f"{attribute_name}")

    def is_clickable_XPATH(self, xpath_selector):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, f"{xpath_selector}")))

    def is_text_present_in_element_XPATH(self, xpath_selector):
        return self.wait.until(EC.text_to_be_present_in_element((By.XPATH, f"{xpath_selector}")))

    def is_value_present_in_attribute_XPATH(self, xpath_selector, attribute, text):
        return self.wait.until(
            EC.text_to_be_present_in_element_attribute((By.XPATH, f"{xpath_selector}"), f"{attribute}", f"{text}"))

    def is_element_present_in_DOM_XPATH(self, xpath_selector):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, f"{xpath_selector}")))

    def is_element_visible_XPATH(self, xpath_selector):
        return self.wait.until(EC.visibility_of_element_located((By.XPATH, f"{xpath_selector}")))

    def finding_elements_XPATH(self, xpath_selector, index):
        elements = self.driver.find_elements(By.XPATH, f"{xpath_selector}")
        return elements[index]

    def list_of_elements_XPATH(self, xpath_selector, index):
        elements = self.driver.find_elements(By.XPATH, f"{xpath_selector}")
        return elements

    def finding_elements_len_XPATH(self, xpath_selector):
        elements = self.driver.find_elements(By.XPATH, f"{xpath_selector}")
        return len(elements)

    def finding_elements_text_XPATH(self, xpath_selector, index):
        elements = self.driver.find_elements(By.XPATH, f"{xpath_selector}")
        return elements[index].text

    def finding_elements_attribute_XPATH(self, xpath_selector, index, attribute):
        elements = self.driver.find_elements(By.XPATH, f"{xpath_selector}")
        return elements[index].get_attribute(f"{attribute}")

    def click_on_each_element_XPATH(self, xpath_selector):
        elements = self.driver.find_elements(By.XPATH, f"{xpath_selector}")
        for each_element in elements:
            each_element.click()

    def getting_text_each_element_XPATH(self, xpath_selector):
        elements = self.driver.find_elements(By.XPATH, f"{xpath_selector}")
        for each_element in elements:
            print(each_element.text)

    def getting_attribute_each_element_XPATH(self, xpath_selector, attribute):
        elements = self.driver.find_elements(By.XPATH, f"{xpath_selector}")
        for each_element in elements:
            print(each_element.get_attribute(f"{attribute}"))

    def switching_to_iframe_XPATH(self, xpath_selector):
        return self.wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, f"{xpath_selector}")))

    def new_webpage(self, url):
        return self.driver.get(f"{url}")

    def back(self):
       return self.driver.back()

    def closing_browser(self):
        return self.driver.close()

    # working with cookies
    def get_cookies(self, file_name):
        with open(f"../reports/{file_name}_cookie.json", "w") as f:
            json.dump(self.driver.get_cookies(), f)

    def load_cookies(self, file_name):
        with open(f"../reports/{file_name}_cookie.json", "rb") as f:
            cookies = json.load(f)
            for cookie in cookies:
                self.driver.add_cookie(cookie)







