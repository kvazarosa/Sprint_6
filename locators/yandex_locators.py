from selenium.webdriver.common.by import By


class YandexLocators:
    # модальное окно
    YANDEX_MODAL = (By.XPATH, "//div[contains(text(), 'Установить Яндекс Браузер?')]")

    #крест на модалке
    MODAL_CLOSE = (By.CSS_SELECTOR, "span[aria-label='Закрыть']")