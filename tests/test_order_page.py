import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import OrderData, Urls
from locators.order_page_locators import OrderPageLocators


class TestOrderPage:
    @allure.title("Оформление заказа")
    @pytest.mark.parametrize(
        "order_data,order_button_locator",
        [
            (OrderData.ORDER_DATA_1, OrderPageLocators.ORDER_BUTTON_UP),
            (OrderData.ORDER_DATA_2, OrderPageLocators.ORDER_BUTTON_DOWN)
        ]
    )
    def test_order_creation(self, driver, order_data, order_button_locator):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.go_to_main_page()
        main_page.accept_cookies()
        main_page.click_element(order_button_locator)

        order_page.fill_first_page(order_data)
        order_page.fill_second_page(order_data)

        result = order_page.confirm_and_check_order()

        assert "Заказ оформлен" in result

    @allure.title("Проверка перехода по логотипу")
    def test_scooter_logo_navigation(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.go_to_main_page()
        main_page.accept_cookies()
        main_page.click_element(OrderPageLocators.ORDER_BUTTON_UP)

        order_page.click_element(OrderPageLocators.SCOOTER_LOGO)
        assert main_page.get_current_url() == Urls.MAIN_PAGE
