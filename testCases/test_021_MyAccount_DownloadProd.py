from pageObjects.HomePage import MainPage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountCustInfo import MyAccountCustInfo
from pageObjects.MyAccountDownloadProdPage import MyAccountDownloadProd
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.SearchPage import SearchPage
from pageObjects.ProdDisplayPage import ProdDisplayPage
from pageObjects.ShoppingCartPage import ShoppingCartPage
from pageObjects.CheckoutPage import CheckoutPage
from utilities.readProperties import ReadConfig
import pytest
from selenium.webdriver.common.by import By
from utilities import randomeString
import time
import os

# TC 006 - validate 'downloadable products' page where the user placed few downloadable products

# Pre-requisites - user is registered - part of the test case.

class Test_021_MyAccountDownloadProd():
    baseURL = ReadConfig.getApplicationURL()
    email = randomeString.random_login_generator() + '@test.com'
    password = ReadConfig.getPassword()
    fname_reg = ReadConfig.fname_reg()
    lname_reg = ReadConfig.lname_reg()
    country = ReadConfig.country()
    city = ReadConfig.city()
    address1 = ReadConfig.address1()
    address2 = ReadConfig.set_address2()
    zipcode = ReadConfig.zipcode()
    phonenum = ReadConfig.phonenum()
    faxnum = ReadConfig.faxnum()
    cardtype = ReadConfig.cardtype()
    cardholdername = ReadConfig.cardholdername()
    cardnumber = ReadConfig.cardnumber()
    expdate_month = ReadConfig.expdate_month()
    expdate_year = ReadConfig.expdate_year()
    cardcode = ReadConfig.cardcode()

    @pytest.mark.myaccount
    def test_download_prod(self, setup):
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

        self.hp.catpage_digital_downloads()
        self.sp = SearchPage(self.driver)

        self.downl_products_list = self.sp.add_to_shopcart_all_prod()

        for r in range(0, len(self.downl_products_list)):
            self.driver.find_element(By.LINK_TEXT, self.downl_products_list[r]).click()
            self.pdp = ProdDisplayPage(self.driver)
            self.pdp.add_to_cart_click()
            self.driver.back()

        self.sp.shopping_cart_click()
        self.scp = ShoppingCartPage(self.driver)
        self.scp.terms_conf_click()
        self.scp.checkout_click()

        self.cop = CheckoutPage(self.driver)
        self.address_conf_msg = self.cop.is_address_saved()
        if self.address_conf_msg == "Select a billing address from your address book or enter a new address.":
            self.cop.use_existing_address_cont()

        else:
            self.cop.set_country(self.country)
            self.cop.city(self.city)
            self.cop.address1(self.address1)
            self.cop.zipcode(self.zipcode)
            self.cop.phonenum(self.phonenum)
            time.sleep(1)
            self.cop.continue_click()

        try:
            if self.cop.shipping_method() == "Shipping method":
                self.cop.continue_shipping_click()
        except:
            None

        self.cop.payment_creditcard_click()
        self.cop.continue4_click()

        self.cop.set_cardtype(self.cardtype)
        self.cop.cardholdername(self.cardholdername)
        self.cop.cardnumber(self.cardnumber)
        self.cop.set_expdate_month(self.expdate_month)
        self.cop.set_expdate_year(self.expdate_year)
        self.cop.cardcode(self.cardcode)
        time.sleep(1)
        self.cop.continue5_click()

        self.cop.confirm_click()
        time.sleep(2)

        self.order = self.cop.ordernb_get()

        self.cop.continue6_click()

        self.hp.myaccount_click()
        self.myci = MyAccountCustInfo(self.driver)
        self.myci.download_prod_click()
        self.mydp = MyAccountDownloadProd(self.driver)

        if self.mydp.down_prod_list_compl() == self.downl_products_list:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_myaccount_downl_prod.png")
            self.driver.close()
            assert False
