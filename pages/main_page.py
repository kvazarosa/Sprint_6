import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from data import Urls


class MainPage(BasePage):
    @allure.step("Принимаем куки")
    def accept_cookies(self):
        WebDriverWait(self.driver, 3).until(
            expected_conditions.element_to_be_clickable(MainPageLocators.COOKIE_LOCATOR)
        ).click()

    @allure.step("Скроллим к разделу с вопросами")
    def scroll_to_questions_section(self):
        anchor = self.find_element_with_wait(MainPageLocators.QUESTION_LOCATOR_TO_SCROLL)
        self.scroll_to_element(anchor)

    @allure.step("Кликаем по вопросу с указанным номером")
    def click_question(self, number):
        question = self.format_locators(MainPageLocators.QUESTION_LOCATOR, number)
        self.click_to_element(question)

    @allure.step("Получаем текст ответа")
    def get_answer_text(self, number):
        answer = self.format_locators(MainPageLocators.RESPONSE_LOCATOR, number)
        return self.get_text_from_element(answer)

    @allure.step("Переходим по указанному URL")
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step("Кликаем на элемент")
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 3).until(
        expected_conditions.element_to_be_clickable(locator)
        ).click()

    @allure.step("Возвращаем корректный URL")
    def is_main_page(self):
        current_url = self.driver.current_url
        return current_url == Urls.MAIN_PAGE
