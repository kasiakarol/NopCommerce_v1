import time
from pageObjects.HomePage import MainPage
from pageObjects.SearchPage import SearchPage
from utilities.readProperties import ReadConfig
import os
import pytest
# TC - Validate the working of 'Community poll' functionality
# It validates 'Community poll' functionality for the unregistered user that is not allowed to vote


class Test_026_CommunityPoll():
    baseURL = ReadConfig.getApplicationURL()
    poll = ReadConfig.poll()

    @pytest.mark.regression
    def test_search(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = MainPage(self.driver)

        if self.poll == "Excellent":
            self.hp.setPollExcellent()
        elif self.poll == "Good":
            self.hp.setPollGood()
        elif self.poll == "Poor":
            self.hp.setPollPoor()
        elif self.poll == "Very bad":
            self.hp.setPollVerybad()

        self.hp.poll_vote_click()
        time.sleep(2)
        if self.hp.poll_error_msg() == "Only registered users can vote.":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_comunnity_poll.png")
            self.driver.close()
            assert False
