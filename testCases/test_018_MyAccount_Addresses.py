import os
import time
from pageObjects.HomePage import MainPage
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchPage import SearchPage
from pageObjects.ShoppingCartPage import ShoppingCartPage
from pageObjects.ProdDisplayPage import ProdDisplayPage
from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.MyAccountCustInfo import MyAccountCustInfo
from pageObjects.MyAccountAddresses import MyAccountAddresses
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities.readProperties import ReadConfig
from utilities import randomeString
import pytest

# TC-015 - Validate new address given for Billing Details while placing the order should get added to My Account > Addresses

# Test is checking if there are any addresses saved in user's account > addresses. If so, it's deleting them.
# Then it's placing the order and validating if the address provided is saved in My Account > Addresses

# Pre-requisites - user is registered - part of the test case.

class Test_018_MyAccountAddresses():
    email = randomeString.random_login_generator() + '@test.com'
    password = ReadConfig.getPassword()
    baseURL = ReadConfig.getApplicationURL()
    search_item = ReadConfig.searchItem()
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
    def test_addresses(self, setup):
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

        self.hp = MainPage(self.driver)
        self.hp.myaccount_click()
        self.myci = MyAccountCustInfo(self.driver)
        self.myci.addresses_click()

        self.myad = MyAccountAddresses(self.driver)


        self.myad.delete_address_click()

        self.myad.home_page_click()

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
        self.cop.continue6_click()

        self.hp.myaccount_click()

        self.myci.addresses_click()


        results = []
        if self.myad.addresses_name_text() == self.fname_reg+" "+self.lname_reg:
            results.append("yes")
        else:
            results.append("no")

        if self.myad.addresses_email_text() == 'Email: ' + self.email:
            results.append("yes")
        else:
            results.append("no")

        if self.myad.addresses_phone_text() == 'Phone number: ' + self.phonenum:
            results.append("yes")
        else:
            results.append("no")

        if self.myad.addresses_fax_text() == 'Fax number:' + self.faxnum:
            results.append("yes")
        else:
            results.append("no")

        if self.myad.addresses_address1_text() == self.address1:
            results.append("yes")
        else:
            results.append("no")

        if self.myad.addresses_cityzip_text() == self.city + ", " +self.zipcode:
            results.append("yes")
        else:
            results.append("no")

        if self.myad.addresses_country_text() == self.country:
            results.append("yes")
        else:
            results.append("no")

        # final validation
        if "no" not in results:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_myaccount_addresses.png")
            self.driver.close()
            assert False


