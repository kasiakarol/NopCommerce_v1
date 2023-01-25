from pageObjects.HomePage import MainPage
from pageObjects.LoginPage import LoginPage
from pageObjects.ForgotPasswordPage import ForgPasswordPage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities.readProperties import ReadConfig
import os
import pytest
from utilities import randomeString

# TC - Validate using Forget Password functionality
# Pre-requisites - user is registered - part of the test case.

class Test_005_ForgotPassword():
    baseURL = ReadConfig.getApplicationURL()
    password = ReadConfig.getPassword()
    user_neg = ReadConfig.getUserEmailNeg()
    fname_reg = ReadConfig.fname_reg()
    lname_reg = ReadConfig.lname_reg()
    email = randomeString.random_login_generator() + '@test.com'

    @pytest.mark.sanity
    def test_forgotpassword(self, setup):
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
        self.lp.forgotPsw()

        self.fpp=ForgPasswordPage(self.driver)
        self.fpp.forgpwdemail(self.email)
        self.fpp.recover_click()

        self.confmsg=self.fpp.bar_conf()

        if self.confmsg == "Email with instructions has been sent to you.":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_forgpwd.png")
            self.driver.close()
            assert False



