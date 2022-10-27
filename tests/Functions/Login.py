"""importing the class LoginPage"""
import time
from PageObject.LoginPage import LoginPage
from Utilities.BaseClass import BaseClass

"""Declared the class"""


class Login(BaseClass):
    """constructor for passing the drivers"""

    def __init__(self, driver):
        self.driver = driver

    """used implicit wait for opening the url and passed the credentials for login """

    def get_login(self, getData):
        self.driver.implicitly_wait(10)
        login = LoginPage(self.driver)
        login.give_email().send_keys(getData["email"])
        login.give_password().send_keys(getData["password"])
        login.click_signin_button().click()
        time.sleep(5)
