from pageObjects.HomePage import MainPage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountCustInfo import MyAccountCustInfo
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.MyAccountRewardPointsPage import MyAccountRewardPoints
from pageObjects.ProdReviewPage import ProdReviewPage
from pageObjects.SearchPage import SearchPage
from pageObjects.ProdDisplayPage import ProdDisplayPage
from pageObjects.MyAccountReviews import MyAccountReviews
from utilities.readProperties import ReadConfig
import pytest
from utilities import randomeString
import os
import time


# TC_001 - validate navigating to 'Reward points' from 'My account' page

# Pre-requisites - user is registered - part of the test case.

class Test_024_MyAccountRewardPoints():
    baseURL = ReadConfig.getApplicationURL()
    password = ReadConfig.getPassword()
    fname_reg = ReadConfig.fname_reg()
    lname_reg = ReadConfig.lname_reg()
    email = randomeString.random_login_generator() + '@test.com'
    search_item = ReadConfig.searchItem()
    rev_title = ReadConfig.revTitle()
    rev_text = ReadConfig.revText()
    rating = ReadConfig.rating()

    @pytest.mark.myaccount
    def test_reward_points(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = MainPage(self.driver)

        self.hp.register()
        self.rp = AccountRegistrationPage(self.driver)

        self.rp.setFirstName(self.fname_reg)
        self.rp.setLastName(self.lname_reg)
        self.email = randomeString.random_login_generator()+'@test.com'
        self.rp.setEmail(self.email)
        self.rp.setPassword(self.password)
        self.rp.setConfirmPassword(self.password)
        self.rp.clickRegister()

        self.hp.login()
        self.lp = LoginPage(self.driver)
        self.lp.insertEmail(self.email)
        self.lp.insertPassword(self.password)
        self.lp.logIn()

        self.hp.myaccount_click()
        self.myci = MyAccountCustInfo(self.driver)
        self.myci.reward_click()
        self.myrp = MyAccountRewardPoints(self.driver)

        if self.myrp.page_title_text() == "My account - Reward points":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_myaccount_rewardpoints.png")
            self.driver.close()
            assert False





