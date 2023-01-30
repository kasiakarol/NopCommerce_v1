import os
import time
from pageObjects.HomePage import MainPage
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchPage import SearchPage
from pageObjects.ShoppingCartPage import ShoppingCartPage
from pageObjects.ProdDisplayPage import ProdDisplayPage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.MyAccountCustInfo import MyAccountCustInfo
from pageObjects.MyAccountOrdersDetails import MyAccountOrdersDetails
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.MyAccountOrders import MyAccountOrders
from utilities.readProperties import ReadConfig
from utilities import randomeString
import pytest

# TC - validates printing invoice in pdf for order from My Account > Orders > Details

# Pre-requisites - user is registered - part of the test case.

class Test_020_MyAccountOrdersDetails():
    email = randomeString.random_login_generator() + '@test.com'
    fname_reg = ReadConfig.fname_reg()
    lname_reg = ReadConfig.lname_reg()
    password = ReadConfig.getPassword()
    baseURL = ReadConfig.getApplicationURL()
    search_item = ReadConfig.searchItem()
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
    def test_orders_details(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        orders = []
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

        self.hp = MainPage(self.driver)
        self.hp.search_txtbox(self.search_item)
        self.hp.search_click()

        self.sp = SearchPage(self.driver)
        self.sp.results_elem_click()

        self.pdp = ProdDisplayPage(self.driver)
        self.pdp.add_to_cart_click()
        self.pdp.addtocart_confmsg_click()

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
        self.myci.orders_click()

        self.myor = MyAccountOrders(self.driver)
        self.myor.details1_click()

        self.myod = MyAccountOrdersDetails(self.driver)
        self.myod.print_invoice_click()


        if self.myod.order_inf_msg()=="Order information":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_order_inf.png")
            self.driver.close()
            assert False

