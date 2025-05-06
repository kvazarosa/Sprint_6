from selenium.webdriver.common.by import By


class OrderPageLocators:
    # Кнопки заказа
    ORDER_BUTTON_UP = (By.XPATH, "(//button[text()='Заказать'])[1]")
    ORDER_BUTTON_DOWN = (By.XPATH, "(//button[text()='Заказать'])[2]")

    # Первая страница формы
    NAME_LOCATOR = (By.XPATH, "//input[@placeholder='* Имя']")
    LAST_NAME_LOCATOR = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_LOCATOR = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    STATION_LOCATOR = (By.XPATH, "//input[@class='select-search__input']")
    STATION_OPTION = (By.CLASS_NAME, "select-search__row")
    PHONE_LOCATOR = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    # кнопка далее
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Вторая страница формы
    CALENDAR_LOCATOR = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_PERIOD_LOCATOR = (By.XPATH, "//div[contains(text(), 'Срок аренды')]")
    RENT_OPTION_1_DAY = (By.XPATH, "//div[text()='сутки']")

    # кнопка заказать
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Content__')]//button[contains(@class, 'Button_Button__ra12g') and text()='Заказать']")

    # кнопка да
    CONFIRM_BUTTON = (By.XPATH, "//button[text()='Да']")

    # текст для закрытия календаря
    RENT_HEADER = (By.XPATH, "//div[contains(text(), 'Про аренду')]")

    # Подтверждение заказа
    ORDER_SUCCESS_LOCATOR = (By.XPATH, "//div[contains(text(), 'Заказ оформлен')]")

    # Логотип самоката
    SCOOTER_LOGO = (By.XPATH, "//a[contains(@class, 'Header_LogoScooter__')]")
