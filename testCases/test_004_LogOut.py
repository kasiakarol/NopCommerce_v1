from pageObjects.HomePage import MainPage
from pageObjects.LoginPage import LoginPage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
import os
from utilities.readProperties import ReadConfig
import pytest
from utilities import randomeString

# TC - Validate log out from the application
# Pre-requisites - user is registered - part of the test case.


class Test_004_LogOut():
    baseURL = ReadConfig.getApplicationURL()
    password = ReadConfig.getPassword()
    fname_reg = ReadConfig.fname_reg()
    lname_reg = ReadConfig.lname_reg()
    email = randomeString.random_login_generator() + '@test.com'

    @pytest.mark.regression
    def test_logout(self, setup):
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
        self.lp=LoginPage(self.driver)
        self.lp.insertEmail(self.email)
        self.lp.insertPassword(self.password)
        self.lp.logIn()
        self.lp.logOut()

        self.myaccount = self.lp.myaccount()
        if not self.myaccount:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_logout.png")
            self.driver.close()
            assert False
