import allure
from selenium.webdriver.common.keys import Keys
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from data import Urls


class OrderPage(BasePage):
    @allure.step("Заполнить первую страницу заказа")
    def fill_first_page(self, order_data):
        self.send_text(OrderPageLocators.NAME_LOCATOR, order_data['name'])
        self.send_text(OrderPageLocators.LAST_NAME_LOCATOR, order_data['last_name'])
        self.send_text(OrderPageLocators.ADDRESS_LOCATOR, order_data['address'])

        station_input = self.find_element(OrderPageLocators.STATION_SEARCH_INPUT)
        station_input.send_keys(order_data['station'])
        station_input.send_keys(Keys.ARROW_DOWN)
        station_input.send_keys(Keys.ENTER)

        self.send_text(OrderPageLocators.PHONE_LOCATOR, order_data['phone'])
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить вторую страницу заказа")
    def fill_second_page(self, order_data):
        self.send_text(OrderPageLocators.CALENDAR_LOCATOR, order_data['date'])
        self.click_element(OrderPageLocators.RENT_HEADER)
        self.click_element(OrderPageLocators.RENT_PERIOD_LOCATOR)
        self.click_element(OrderPageLocators.RENT_OPTION_1_DAY)

        order_button = self.wait_for_element_to_be_clickable(OrderPageLocators.ORDER_BUTTON)
        order_button.click()

    @allure.step("Подтвердить заказ и проверить успешность")
    def confirm_and_check_order(self):
        confirm_button = self.wait_for_element_to_be_clickable(OrderPageLocators.CONFIRM_BUTTON)
        confirm_button.click()

        success_element = self.wait_for_element_to_be_visible(OrderPageLocators.ORDER_SUCCESS_LOCATOR)
        return success_element.text

    @allure.step("Проверить переход на главную страницу")
    def verify_main_page_navigation(self):
        self.click_element(OrderPageLocators.SCOOTER_LOGO)
        self.wait_for_url(Urls.MAIN_PAGE)
