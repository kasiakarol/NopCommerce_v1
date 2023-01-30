import os
import time
from pageObjects.HomePage import MainPage
from pageObjects.SearchPage import SearchPage
from pageObjects.ShoppingCartPage import ShoppingCartPage
from pageObjects.ProdDisplayPage import ProdDisplayPage
from pageObjects.CheckoutPage import CheckoutPage
from utilities.readProperties import ReadConfig
import pytest

# TC 016 - validate checkout as a guest - fill in all the fields

class Test_015_Checkout():
    baseURL = ReadConfig.getApplicationURL()
    search_item = ReadConfig.searchItem()
    fname = ReadConfig.fname()
    lname = ReadConfig.lname()
    email_checkout = ReadConfig.email_checkout()
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

    @pytest.mark.sanity
    def test_checkout(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

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
        self.cop.checkout_as_guest_click()
        self.cop.fname(self.fname)
        self.cop.lname(self.lname)
        self.cop.email(self.email_checkout)
        self.cop.set_country(self.country)
        self.cop.city(self.city)
        self.cop.address1(self.address1)
        self.cop.address2(self.address2)
        self.cop.zipcode(self.zipcode)
        self.cop.phonenum(self.phonenum)
        self.cop.faxnum(self.faxnum)
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

        if self.cop.getconfirmmsg() == "Your order has been successfully processed!":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_checkout.png")
            self.driver.close()
            assert False


