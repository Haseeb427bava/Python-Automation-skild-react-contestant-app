import time
import pytest
from PageObject.ProfilePage import ProfilePage
from PageObject.TeamPage import TeamPage
from TestData.Data import Data
from Utilities.BaseClass import BaseClass
from tests.Functions.AddTeamMember import Team
from tests.Functions.Login import Login

"""class for assertion and no of test cases"""


class TestTeam(BaseClass):
    """Login tests and their assertion"""

    def test_team(self, getData, gotData):
        login = Login(self.driver)
        login.get_login(getData)
        time.sleep(1)
        self.clickLink("Team")
        team_add = Team(self.driver)
        team_add.team_page(gotData)
        team = TeamPage(self.driver)
        button = team.team_delete_button()
        assert (button.is_displayed())
        button.click()
        team.team_yes_button().click()


@pytest.fixture(params=Data.Login_data)
def getData(request):
    return request.param


@pytest.fixture(params=Data.Team_data)
def gotData(request):
    return request.param
