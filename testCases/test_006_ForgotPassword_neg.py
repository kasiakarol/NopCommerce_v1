from pageObjects.HomePage import MainPage
from pageObjects.LoginPage import LoginPage
from pageObjects.ForgotPasswordPage import ForgPasswordPage
from utilities.readProperties import ReadConfig
import os
import pytest

# TC - Validate using Forget Password functionality for invalid email address

class Test_006_ForgotPasswordNeg():
    baseURL = ReadConfig.getApplicationURL()
    user = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()
    user_neg = ReadConfig.getUserEmailNeg()

    @pytest.mark.regression
    def test_forgotpasswordneg(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp=MainPage(self.driver)
        self.hp.login()

        self.lp=LoginPage(self.driver)
        self.lp.forgotPsw()

        self.fpp=ForgPasswordPage(self.driver)
        self.fpp.forgpwdemail(self.user_neg)
        self.fpp.recover_click()

        self.confmsg_neg=self.fpp.bar_conf_neg()

        if self.confmsg_neg == "Email not found.":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_forgpwd_neg.png")
            self.driver.close()
            assert False