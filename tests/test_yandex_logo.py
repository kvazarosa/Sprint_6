import pytest
import allure
from pages.main_page import MainPage
from pages.yandex_logo_page import YandexLogoPage


class TestYandexLogo:
    @allure.title('Проверка кнопки "Да" в модальном окне Дзена')
    def test_dzen_modal_yes_button(self, driver):
        main_page = MainPage(driver)
        yandex_page = YandexLogoPage(driver)

        allure.step("Открыть главную страницу")
        main_page.go_to_main_page()
        main_page.accept_cookies()

        allure.step("Кликнуть на логотип Яндекса")
        main_page.click_yandex_logo()

        allure.step("Проверить кнопку 'Да' в модальном окне")
        assert yandex_page.check_dzen_modal_yes_button()
