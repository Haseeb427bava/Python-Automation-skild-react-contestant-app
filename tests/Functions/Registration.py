"""importing the class LoginPage"""
import time
from PageObject.LoginPage import LoginPage
from Utilities.BaseClass import BaseClass

"""Declared the class"""


class Registration(BaseClass):
    """constructor for passing the drivers"""

    def __init__(self, driver):
        self.driver = driver

    """Correct Registration"""

    def correct_registration(self, getData):
        # log = self.getLogger()
        self.driver.implicitly_wait(5)
        login = LoginPage(self.driver)
        registrationpage = login.click_signup_link_text()
        time.sleep(1)
        registrationpage.give_first_name().send_keys(getData["firstname"])
        registrationpage.select_check_box_reading().click()
        registrationpage.select_check_box_writing().click()
        registrationpage.select_check_box_playing().click()
        time.sleep(1)
        registrationpage.give_last_name().send_keys(getData["lastname"])
        time.sleep(1)
        registrationpage.give_team_name().send_keys(getData["team_name"])
        time.sleep(1)
        registrationpage.give_email().send_keys(getData["email"])
        time.sleep(1)
        registrationpage.give_create_password().send_keys(getData["password"])
        time.sleep(1)
        registrationpage.give_confirm_password().send_keys(getData["password"])
        time.sleep(1)
        registrationpage.click_button()

    def give_wrong_registration(self, getData):
        self.driver.implicitly_wait(5)
        login = LoginPage(self.driver)
        registrationpage = login.click_signup_link_text()
        time.sleep(1)
        registrationpage.give_first_name().send_keys(getData["firstname"])
        registrationpage.select_check_box_reading().click()
        registrationpage.select_check_box_writing().click()
        registrationpage.select_check_box_playing().click()
        time.sleep(1)
        registrationpage.give_last_name().send_keys(getData["lastname"])
        time.sleep(1)
        registrationpage.give_team_name().send_keys(getData["team_name"])
        time.sleep(1)
        registrationpage.give_email().send_keys(getData["email"])
        time.sleep(1)
        registrationpage.give_create_password().send_keys(getData["password"])
        time.sleep(1)
        registrationpage.give_confirm_password().send_keys(getData["password"])
        time.sleep(1)
        registrationpage.click_button()
