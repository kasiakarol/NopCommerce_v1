import time
from pageObjects.HomePage import MainPage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountCustInfo import MyAccountCustInfo
from pageObjects.MyAccountPwdChangePage import MyAccountPwdChange
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
import os
from utilities.readProperties import ReadConfig
from utilities import randomeString
import pytest

# TC_CP_004 - Validate entering different password into the 'Password' and 'Password Confirm' fields while changing password
# Pre-requisites - user is registered.

class Test_017_PasswordChange():
    baseURL = ReadConfig.getApplicationURL()
    password = ReadConfig.getPassword()
    oldpwd = ReadConfig.oldpwd()
    newpwd = ReadConfig.newpwd()
    confirmpwd = ReadConfig.confirmpwd()
    fname_reg = ReadConfig.fname_reg()
    lname_reg = ReadConfig.lname_reg()
    email = randomeString.random_login_generator() + '@test.com'

    @pytest.mark.myaccount
    def test_pwd_change(self, setup):
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
        self.hp.myaccount_click()

        self.myci = MyAccountCustInfo(self.driver)

        self.myci.pwd_change_click()

        self.mypc = MyAccountPwdChange(self.driver)
        self.mypc.old_pwd(self.password)
        self.mypc.new_pwd(self.newpwd)
        self.mypc.confirm_pwd(self.confirmpwd)
        self.mypc.change_pwd_click()

        if self.mypc.msg_pwdchange_error_text() == "The new password and confirmation password do not match.":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_myaccount_pwdchange.png")
            self.driver.close()
            assert False


