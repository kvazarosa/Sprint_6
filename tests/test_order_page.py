import pytest
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data import OrderData, Urls
from locators.order_page_locators import OrderPageLocators
import allure


class TestOrderPage:
    @pytest.mark.parametrize(
        'order_button_locator, order_data',
        [
            (OrderPageLocators.ORDER_BUTTON_UP, OrderData.ORDER_DATA_1),
            (OrderPageLocators.ORDER_BUTTON_DOWN, OrderData.ORDER_DATA_2)
        ]
    )
    @allure.title('Проверка на создание заказа')
    def test_create_order(self, driver, order_button_locator, order_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.go_to_url(Urls.MAIN_PAGE)
        main_page.accept_cookies()
        main_page.click_to_element(order_button_locator)
        order_page.fill_first_page(order_data)
        order_page.fill_second_page(order_data)
        order_page.confirm_order()

        assert "Заказ оформлен" in order_page.check_success_order()

    @allure.title('При клике на логотип самоката переходим на главную страницу')
    def test_scooter_logo_navigation(self, driver):  # Добавлен self
        main_page = MainPage(driver)
        main_page.go_to_url(Urls.ORDER_PAGE)
        main_page.click_to_element(OrderPageLocators.SCOOTER_LOGO)
        assert main_page.is_main_page()
