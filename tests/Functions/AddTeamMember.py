import time
from PageObject.TeamPage import TeamPage
from Utilities.BaseClass import BaseClass


class Team(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    def team_page(self, gotData):
        team = TeamPage(self.driver)
        time.sleep(4)
        team.team_name_edit_butt().click()
        self.sending_key(team.team_name(), gotData["team_name"])
        team.confirm_team_name().click()
        self.clickLink("Add a Team Member")
        self.sending_key(team.team_member_first_name(), gotData["firstname"])
        self.sending_key(team.team_member_last_name(), gotData["lastname"])
        self.sending_key(team.team_member_email(), gotData["email"])
        self.sending_key(team.team_member_message(), gotData["message"])
        team.team_member_save_button().click()


