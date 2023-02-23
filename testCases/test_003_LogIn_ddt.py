import time
import pytest
from pageObjects.HomePage import MainPage
from pageObjects.LoginPage import LoginPage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities import XLUtils
from utilities.readProperties import ReadConfig

# TC_LF_002 Validate login to the application using invalid credentials
# This test case use data driven testing with Excel


class Test_003_LogIn_DDT():
    baseURL = ReadConfig.getApplicationURL()
    fname_reg = ReadConfig.fname_reg()
    lname_reg = ReadConfig.lname_reg()

    path = "C:\\Users\\kasia\\PycharmProjects\\NopCommerce_v1\\testData\\nopCommerce_LoginData.xlsx"

    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.rows=XLUtils.getRowCount(self.path, 'List1')
        lst_status=[] #list to store 'Pass' or 'Fail' in order to verify the final result

        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = MainPage(self.driver)
        self.lp = LoginPage(self.driver)
        self.rp = AccountRegistrationPage(self.driver)

        # Pre-requisites - user is registered
        for r in range(2, 4):
            self.hp.register()

            self.email = XLUtils.readData(self.path, "List1", r, 1)
            self.password = XLUtils.readData(self.path, "List1", r, 2)
            self.exp = XLUtils.readData(self.path, "List1", r, 3)

            self.rp.setFirstName(self.fname_reg)
            self.rp.setLastName(self.lname_reg)
            self.rp.setEmail(self.email)
            self.rp.setPassword(self.password)
            self.rp.setConfirmPassword(self.password)
            self.rp.clickRegister()

            time.sleep(2)

        # Login validation
        for r in range(2, self.rows+1):
            self.hp.login()

            self.email = XLUtils.readData(self.path, "List1", r, 1)
            self.password = XLUtils.readData(self.path, "List1", r, 2)
            self.exp = XLUtils.readData(self.path, "List1", r, 3)

            self.lp.insertEmail(self.email)
            self.lp.insertPassword(self.password)
            self.lp.logIn()
            time.sleep(3)
            self.myaccount = self.lp.myaccount()

            if self.exp == "valid":
                if self.myaccount == True:
                    lst_status.append("Pass")
                    self.hp.logout_click()
                else:
                    lst_status.append("Fail")
            elif self.exp == "invalid":
                if self.myaccount == False:
                    lst_status.append("Pass")
                elif self.myaccount == True:
                    lst_status.append("Fail")
        self.driver.close()
        # final validation
        if "Fail" not in lst_status:
            assert True
        else:
            assert False



