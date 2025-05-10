from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def find_element(self, locator):
        return WebDriverWait(self.driver, 3).until(
            EC.visibility_of_element_located(locator)
        )

    def click_element(self, locator):
        WebDriverWait(self.driver, 3).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def send_text(self, locator, text):
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)

    def get_element_text(self, locator):
        return self.find_element(locator).text

    def accept_cookies(self):
        self.click_element(MainPageLocators.COOKIE_LOCATOR)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def format_locators(self, locator_0, number):
        method, locator = locator_0
        locator = locator.format(number)
        return (method, locator)

    def switch_to_new_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])


    def get_current_url(self):
        return self.driver.current_url

    def wait_for_element_to_be_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_url(self, url, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.url_to_be(url)
        )

    def wait_for_element_to_be_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )
