from selenium.webdriver.support import expected_conditions
from locators.yandex_locators import YandexLocators
from pages.main_page import MainPage
from pages.yandex_logo_page import YandexLogoPage
from data import Urls
import allure


class TestYandexLogo:
    @allure.title('При клике на логотип яндекса попадаем на яндекс дзен')
    def test_yandex_modal_appears_after_redirect(self, driver):
        main_page = MainPage(driver)
        yandex_page = YandexLogoPage(driver)
        main_page.go_to_url(Urls.MAIN_PAGE)
        main_page.accept_cookies()
        yandex_page.click_yandex_logo()
        driver.switch_to.window(driver.window_handles[1])
        modal = yandex_page.wait.until(
            expected_conditions.visibility_of_element_located(YandexLocators.YANDEX_MODAL))
        assert modal.is_displayed(), "Модальное окно не отображается"
        assert "Установить Яндекс Браузер?" in modal.text, "Неверный текст в модалке"
