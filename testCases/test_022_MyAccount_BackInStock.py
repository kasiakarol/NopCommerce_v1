from pageObjects.HomePage import MainPage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountCustInfo import MyAccountCustInfo
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.MyAccountBackInStockPage import MyAccountBackInStock
from utilities.readProperties import ReadConfig
import pytest
from utilities import randomeString
import os

# TC 006 - validate 'Back in stock' page where the user has not received any feedback about back in stock products

# Pre-requisites - user is registered - part of the test case.

class Test_022_MyAccountBackInStock():
    baseURL = ReadConfig.getApplicationURL()
    password = ReadConfig.getPassword()
    fname_reg = ReadConfig.fname_reg()
    lname_reg = ReadConfig.lname_reg()
    email = randomeString.random_login_generator() + '@test.com'

    @pytest.mark.myaccount
    def test_back_in_stock(self, setup):
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
        self.myci.back_in_stock_click()
        self.mybi = MyAccountBackInStock(self.driver)

        results = []
        if self.mybi.page_title_text() == "My account - Back in stock subscriptions":
            results.append("yes")
        else:
            results.append("no")

        if self.mybi.msg_nodata_text() == "You are not currently subscribed to any Back In Stock notification lists":
            results.append("yes")
        else:
            results.append("no")

        #final validation:
        if "no" not in results:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_myaccount_backinstock.png")
            self.driver.close()
            assert False
