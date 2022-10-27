"""it manages all the properties in the home page"""
from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    PARAGRAPH_TEXT = (By.XPATH, '//*[@id="main"]/div[2]/div/div[1]/div[1]')
    EVENT_STATUS = (By.CSS_SELECTOR, "main[id='main'] div div div h2")
    TIME_LEFT_TO_SUBMIT = (By.XPATH, "")
    PHASE_ONE = (By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/div[1]/div[2]/div/div/p/span[2]')
    DROP_DOWN = (By.XPATH, '//*[@id="category-select"]')
    ANIMAL_LIST = (By.XPATH, '//*[@id="menu-"]/div[3]/ul/li')
    OPTION = (By.XPATH, '//*[@id="menu-"]/div[3]/ul/li[5]')
    BUTTON = (By.XPATH, '//*[@id="main"]/div[2]/div/div[2]/button')
    TEXT = (By.XPATH, '//*[@id="category-select"]')

    """"""

    def home_page_paragraph_text(self):
        return self.driver.find_element(*HomePage.PARAGRAPH_TEXT)

    def getDropdown(self):
        return self.driver.find_element(*HomePage.DROP_DOWN)

    def home_page_button(self):
        return self.driver.find_element(*HomePage.BUTTON)

    def home_page_option(self):
        return self.driver.find_element(*HomePage.OPTION)

    def home_page_text(self):
        return self.driver.find_element(*HomePage.TEXT)

    def home_page_animal_list(self):
        return self.driver.find_elements(*HomePage.ANIMAL_LIST)
