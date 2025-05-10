from selenium.webdriver.common.by import By


class YandexLocators:
    YANDEX_LOGO = (By.CSS_SELECTOR, "a.Header_LogoYandex__3TSOI")
    DZEN_MODAL_YES_BUTTON = (By.XPATH, "//a[@title='Да' and contains(@class, 'vadfaf85a')]")