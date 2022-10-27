import time
from PageObject.ProfilePage import ProfilePage
from Utilities.BaseClass import BaseClass


class Profile(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def profile_page(self, gotData):
        profile = ProfilePage(self.driver)
        time.sleep(4)
        self.sending_key(profile.profile_first_name(), gotData["First_Name"])
        self.sending_key(profile.profile_last_name(), gotData["Last_Name"])
        profile.profile_name_update_button().click()
