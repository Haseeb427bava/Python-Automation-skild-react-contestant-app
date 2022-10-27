"""importing the BaseClass and Login class"""
import time
import pytest
from TestData.Data import Data
from Utilities.BaseClass import BaseClass
from tests.Functions.Login import Login


"""class for assertion and no of test cases"""


class TestContestantApp(BaseClass):
    """Login tests and their assertion"""

    def test_login(self, getData):
        login = Login(self.driver)
        login.get_login(getData)
        time.sleep(5)
        actual_url = self.driver.current_url
        expected_url = "https://contestant-dev.skild.com/home"
        assert actual_url == expected_url


@pytest.fixture(params=Data.Login_data)
def getData(request):
    return request.param
