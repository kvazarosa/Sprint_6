from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = (By.XPATH, '//*[@id="accordion__heading-{}"]')
    RESPONSE_LOCATOR = (By.XPATH, '//*[@id="accordion__panel-{}"]')
    QUESTION_LOCATOR_TO_SCROLL = (By.XPATH, '//*[@id="accordion__heading-7"]')
    COOKIE_LOCATOR = (By.XPATH, '//*[@id="rcc-confirm-button"]')
    YANDEX_LOGO = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")
    ORDER_BUTTON_UP = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_BUTTON_DOWN = (By.XPATH, "(//button[text()='Заказать'])[2]")