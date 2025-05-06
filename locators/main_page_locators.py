from selenium.webdriver.common.by import By


class MainPageLocators:
    #  вопросы и ответы
    QUESTION_LOCATOR = By.XPATH, '//*[@id="accordion__heading-{}"]'
    RESPONSE_LOCATOR = By.XPATH, '//*[@id="accordion__panel-{}"]'

    # самый нижний вопрос
    QUESTION_LOCATOR_TO_SCROLL = By.XPATH, '//*[@id="accordion__heading-7"]'

    # куки
    COOKIE_LOCATOR = By.XPATH, '//*[@id="rcc-confirm-button"]'

    # Логотип яндекса
    YANDEX_LOGO = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")