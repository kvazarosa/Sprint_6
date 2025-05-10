from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Кнопки заказа
    ORDER_BUTTON_UP = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_BUTTON_DOWN = (By.XPATH, "(//button[text()='Заказать'])[2]")

    # Первая страница
    NAME_LOCATOR = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_LOCATOR = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_LOCATOR = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    STATION_SEARCH_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    STATION_OPTION = (By.XPATH, "//div[contains(@class, 'select-search__option') and contains(text(), '{}')]")
    PHONE_LOCATOR = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая страница
    CALENDAR_LOCATOR = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_HEADER = (By.XPATH, "//div[contains(text(), 'Про аренду')]")
    RENT_PERIOD_LOCATOR = (By.XPATH, "//div[contains(text(), 'Срок аренды')]")
    RENT_OPTION_1_DAY = (By.XPATH, "//div[text()='сутки']")
    ORDER_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")

    CONFIRM_BUTTON = (By.XPATH, ".//button[text()='Да']")
    ORDER_SUCCESS_LOCATOR = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")

    # Навигация
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter__')]")