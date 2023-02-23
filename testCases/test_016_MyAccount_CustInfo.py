import os
from pageObjects.HomePage import MainPage
from pageObjects.LoginPage import LoginPage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.MyAccountCustInfo import MyAccountCustInfo
from utilities.readProperties import ReadConfig
import time
import pytest
from utilities import randomeString

# TC_MAI_007 - Validate Page Heading, Page Title and Page URL in the 'Customer info' page

# Pre-requisites - user is registered - part of the test case.

class Test_016_MyAccount_CustInfo():
    baseURL = ReadConfig.getApplicationURL()
    password = ReadConfig.getPassword()
    fname_reg = ReadConfig.fname_reg()
    lname_reg = ReadConfig.lname_reg()
    email = randomeString.random_login_generator() + '@test.com'

    @pytest.mark.myaccount
    def test_myaccount_custinfo(self, setup):
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
        time.sleep(2)
        self.myci = MyAccountCustInfo(self.driver)

        results = []
        if self.driver.title == "nopCommerce demo store. Account":
            results.append("yes")
        else:
            results.append("no")

        if self.driver.current_url == "https://demo.nopcommerce.com/customer/info":
            results.append("yes")
        else:
            results.append("no")

        if self.myci.page_heading_text() == "My account - Customer info":
            results.append("yes")
        else:
            results.append("no")

        # final validation
        if "no" not in results:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_myaccount_custinfo.png")
            self.driver.close()
            assert False


