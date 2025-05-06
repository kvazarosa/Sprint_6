import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class OrderPage(BasePage):
    @allure.step("Вводим данные на первой странице")
    def fill_first_page(self, order_data):
        self.add_text_to_element(OrderPageLocators.NAME_LOCATOR, order_data['name'])
        self.add_text_to_element(OrderPageLocators.LAST_NAME_LOCATOR, order_data['last_name'])
        self.add_text_to_element(OrderPageLocators.ADDRESS_LOCATOR, order_data['address'])

        self.click_to_element(OrderPageLocators.STATION_LOCATOR)
        self.click_to_element((By.XPATH, f"//*[text()='{order_data['station']}']"))

        self.add_text_to_element(OrderPageLocators.PHONE_LOCATOR, order_data['phone'])
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Вводим данные на второй странице")
    def fill_second_page(self, order_data):
        self.add_text_to_element(OrderPageLocators.CALENDAR_LOCATOR, order_data['date'])
        self.click_to_element(OrderPageLocators.RENT_HEADER)
        self.click_to_element(OrderPageLocators.RENT_PERIOD_LOCATOR)
        self.click_to_element(OrderPageLocators.RENT_OPTION_1_DAY)
        self.click_to_element(OrderPageLocators.ORDER_BUTTON)

    @allure.step("Кликаем в окне на кнопку 'Да'")
    def confirm_order(self):
        self.click_to_element(OrderPageLocators.CONFIRM_BUTTON)

    @allure.step("Получаем текст 'Заказ оформлен'")
    def check_success_order(self):
        return WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(OrderPageLocators.ORDER_SUCCESS_LOCATOR)
        ).text
