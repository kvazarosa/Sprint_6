from pages.base_page import BasePage
from locators.yandex_locators import YandexLocators
import allure


class YandexLogoPage(BasePage):
    @allure.step("Нажать на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(YandexLocators.YANDEX_LOGO)

    @allure.step("Проверить кнопку 'Да' в модальном окне")
    def check_dzen_modal_yes_button(self):
        self.switch_to_new_window()
        return self.wait_for_element_to_be_visible(
            YandexLocators.DZEN_MODAL_YES_BUTTON
        ).is_displayed()
