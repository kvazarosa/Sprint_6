from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.main_page_locators import MainPageLocators
import allure


class YandexLogoPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Кликаем на логотип Яндекса")
    def click_yandex_logo(self):
        self.wait.until(
            expected_conditions.element_to_be_clickable(MainPageLocators.YANDEX_LOGO)
        ).click()
