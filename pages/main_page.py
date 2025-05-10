from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data import Urls
import allure


class MainPage(BasePage):
    @allure.step("Открыть главную страницу")
    def go_to_main_page(self):
        self.driver.get(Urls.MAIN_PAGE)

    @allure.step("Кликнуть на логотип Яндекса")
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    @allure.step("Скроллить к вопросам")
    def scroll_to_questions(self):
        question = self.find_element(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.scroll_to_element(question)

    @allure.step("Открыть вопрос")
    def open_question(self, number):
        locator = self.format_locators(MainPageLocators.QUESTION_LOCATOR, number)
        self.click_element(locator)

    @allure.step("Получить текст ответа")
    def get_answer_text(self, number):
        locator = self.format_locators(MainPageLocators.RESPONSE_LOCATOR, number)
        return self.get_element_text(locator)
