"""it manages all the properties in the home page"""
from selenium.webdriver.common.by import By


class CatsFormPage:
    def __init__(self, driver):
        self.driver = driver

    CATEGORY_SELECT = (By.CSS_SELECTOR, "#category-select")
    TITLE_SUBMISSION = (By.XPATH, '//*[@id="main"]/form/div/div[4]/div/div/div[2]/div/input')
    TEST_FIELD1 = (By.CSS_SELECTOR, "input[aria-label='test field 1 Characters 0/20 ']")
    TEST_FIELD2 = (By.CSS_SELECTOR, "input[aria-label='test field 1 Characters 0/20 ']")
    TEST_RICH = (By.XPATH, '//*[@id="main"]/form/div/div[7]/div/div/div[2]/div[3]/div')
    ABOUT_CAT = (By.XPATH, '//*[@id="main"]/form/div/div[9]/div/div/div[2]/div[3]/div')
    YOUTUBE_URL = (By.XPATH, '//*[@id="main"]/form/div/div[10]/div/div/div[2]/div/input')
    CAT_RADIO_BUTTON = (By.XPATH, '//*[@id="main"]/form/div/div[12]/div/div/div[2]')
    CAT_FORM_CHECKBOX = (By.XPATH, '//*[@id="main"]/form/div/div[15]/div/fieldset/div')
    TEXT = (By.XPATH, '//*[@id="category-select"]')

    """"""

    def form_assertion(self):
        return self.driver.find_element(*CatsFormPage.CATEGORY_SELECT)

    def form_title_submission(self):
        return self.driver.find_element(*CatsFormPage.TITLE_SUBMISSION)

    def form_test_field1(self):
        return self.driver.find_element(*CatsFormPage.TEST_FIELD1)

    def form_test_field2(self):
        return self.driver.find_element(*CatsFormPage.TEST_FIELD2)

    def rich_text(self):
        return self.driver.find_element(*CatsFormPage.TEST_RICH)

    def about_cat(self):
        return self.driver.find_element(*CatsFormPage.ABOUT_CAT)

    def youtube_url(self):
        return self.driver.find_element(*CatsFormPage.YOUTUBE_URL)

    def cat_checkbox(self):
        return self.driver.find_element(*CatsFormPage.CAT_FORM_CHECKBOX)

    def cat_radio_button(self):
        return self.driver.find_element(*CatsFormPage.CAT_RADIO_BUTTON)

    def cat_text(self):
        return self.driver.find_elements(*CatsFormPage.TEXT)
