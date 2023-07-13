from selenium.webdriver.common.by import By


class TextBoxPageLocators:

    FULL_NAME = (By.XPATH, '//input[@id="userName"]')
    EMAIL = (By.XPATH, '//input[@id="userEmail"]')
    Current_Address = (By.XPATH, '//textarea[@id="currentAddress"]')
    PERMANENT_ADRESS = (By.XPATH, '//textarea[@id="permanentAddress"]')
    SUBMIT = (By.XPATH, '//button[@id="submit"]')

    CREATED_FULL_NAME = (By.CSS_SELECTOR, '#output #name')
    CREATED_EMAIL = (By.CSS_SELECTOR, '#output #email')
    CREATED_Current_Address = (By.CSS_SELECTOR, '#output #currentAddress')
    CREATED_PERMANENT_ADRESS = (By.CSS_SELECTOR, '#output #permanentAddress')

class CheckBoxPageLocators:

    EXPAND_ALL_BUTTON = (By.XPATH, '//button[@title="Expand all"]')
    ITEM_LIST = (By.XPATH, '//span[@class="rct-title"]')
    CHECKED_ITEMS = (By.CSS_SELECTOR, 'svg[class="rct-icon rct-icon-check"]')
    TITLE_ITEM = ("//ancestor::span[@class='rct-text']")

class RadioButtonPageLocators:

    YES = (By.XPATH, '//label[@for="yesRadio"]')
    IMPRESSIVE = (By.XPATH, '//label[@for="impressiveRadio"]')
    NO = (By.XPATH, '//label[@for="noRadio"]')
    OUTPUT_RESULT = (By.CSS_SELECTOR, 'p span[class="text-success"]')
