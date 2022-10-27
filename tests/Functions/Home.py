import time
from PageObject.HomePage import HomePage
from Utilities.BaseClass import BaseClass


class Home(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def homepage(self, gotData):
        homepage = HomePage(self.driver)
        time.sleep(4)
        homepage.getDropdown().click()
        self.selectCheckBox(homepage.home_page_animal_list(), gotData["Animal"])
        time.sleep(4)
        homepage.home_page_button().click()
