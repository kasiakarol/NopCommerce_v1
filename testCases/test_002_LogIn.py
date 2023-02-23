import time
from pageObjects.HomePage import MainPage
from pageObjects.LoginPage import LoginPage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
import os
from utilities.readProperties import ReadConfig
import pytest
from utilities import randomeString

# TC_LF_001 - Validate logging into the application, using valid credentials
# Pre-requisites - user is registered - part of the test case.


class Test_002_LogIn():
    baseURL = ReadConfig.getApplicationURL()
    password = ReadConfig.getPassword()
    fname_reg = ReadConfig.fname_reg()
    lname_reg = ReadConfig.lname_reg()
    email = randomeString.random_login_generator() + '@test.com'

    @pytest.mark.sanity
    def test_login(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = MainPage(self.driver)
        self.hp.register()
        self.rp = AccountRegistrationPage(self.driver)

        self.rp.setFirstName(self.fname_reg)
        self.rp.setLastName(self.lname_reg)
        self.rp.setEmail(self.email)
        self.rp.setPassword(self.password)
        self.rp.setConfirmPassword(self.password)
        self.rp.clickRegister()

        self.hp.login()

        self.lp = LoginPage(self.driver)
        self.lp.insertEmail(self.email)
        self.lp.insertPassword(self.password)
        self.lp.logIn()

        self.myaccount = self.lp.myaccount()

        if self.myaccount == True:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
