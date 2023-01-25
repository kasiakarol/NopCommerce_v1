from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CheckoutPage():
    btn_checkoutasguest_xpath = "//button[normalize-space()='Checkout as Guest']"
    btn_register_xpath = "//button[normalize-space()='Register']"
# Billing address
    msg_address_exists = "//label[contains(text(),'Select a billing address from your address book or')]"
    btn_cont_use_existaddress_xpath = "//button[@onclick='Billing.save()']"
    checkbox_shiptothesameaddress_name = "ShipToSameAddress"
    txtbox_fname_id = "BillingNewAddress_FirstName"
    txtbox_lname_id = "BillingNewAddress_LastName"
    txtbox_email_id = "BillingNewAddress_Email"
    txtbox_company_name = "BillingNewAddress.Company"
    dpd_country_xapth = "//select[@id='BillingNewAddress_CountryId']"
    txtbox_city_id = "BillingNewAddress_City"
    txtbox_address1_id = "BillingNewAddress_Address1"
    txtbox_address2_id = "BillingNewAddress_Address2"
    txtbox_zipcode_id = "BillingNewAddress_ZipPostalCode"
    txtbox_phonenum_id = "BillingNewAddress_PhoneNumber"
    txtbox_faxnum_id = "BillingNewAddress_FaxNumber"
    btn_continue_xpath = "//button[@onclick='Billing.save()']"

# Shipping method
    rb_ground_xpath = "//input[@id='shippingoption_0']"
    rb_nextdayair_xpath = "//input[@id='shippingoption_1']"
    rb_2nddayair_xpath = "//input[@id='shippingoption_2']"
    btn_continue3_xpath = "//button[@class='button-1 shipping-method-next-step-button']"

# Payment method
    rb_check_xpath = "//input[@id='paymentmethod_0']"
    rb_creditcard_xpath = "//input[@id='paymentmethod_1']"
    btn_continue4_xpath = "//button[@class='button-1 payment-method-next-step-button']"

# Payment method for credit card method
    dpd_cardtype_xpath = "//select[@id='CreditCardType']"
    txtbox_cardholdername_name = "CardholderName"
    txtbox_cardnumber_name = "CardNumber"
    dpd_expdate_month_xpath = "//select[@id='ExpireMonth']"
    dpd_expdate_year_xpath = "//select[@id='ExpireYear']"
    txtbox_cardcode_xpath = "//input[@id='CardCode']"
    btn_continue5_xpath = "//button[@class='button-1 payment-info-next-step-button']"

# Confirm order
    btn_confirm_xpath = "//button[normalize-space()='Confirm']"
    text_order_processed_conf_xpath = "//strong[normalize-space()='Your order has been successfully processed!']"
    btn_continue6_xpath = "//button[normalize-space()='Continue']"
    txt_ordernb_xpath = "//strong[contains(.,'Order number:')]"

#constructor:
    def __init__(self,driver):
        self.driver=driver

    def checkout_as_guest_click(self):
        self.driver.find_element(By.XPATH, self.btn_checkoutasguest_xpath).click()

    def register_click(self):
        self.driver.find_element(By.XPATH, self.btn_register_xpath).click()

# Billing address
    def is_address_saved(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_address_exists).text
        except:
            None

    def use_existing_address_cont(self):
        self.driver.find_element(By.XPATH, self.btn_cont_use_existaddress_xpath).click()

    def shiptothesameaddress_click(self):
        self.driver.find_element(By.XPATH, self.checkbox_shiptothesameaddress_name).click()

    def fname(self, fname):
        self.driver.find_element(By.ID, self.txtbox_fname_id).send_keys(fname)

    def lname(self, lname):
        self.driver.find_element(By.ID, self.txtbox_lname_id).send_keys(lname)

    def email(self, email_checkout):
        self.driver.find_element(By.ID, self.txtbox_email_id).send_keys(email_checkout)

    def set_country(self, country):
        self.country = Select(self.driver.find_element(By.XPATH,self.dpd_country_xapth))
        self.country.select_by_visible_text(country)

    def city(self, city):
        self.driver.find_element(By.ID, self.txtbox_city_id).send_keys(city)

    def address1(self, address1):
        self.driver.find_element(By.ID, self.txtbox_address1_id).send_keys(address1)

    def address2(self, address2):
        self.driver.find_element(By.ID, self.txtbox_address2_id).send_keys(address2)

    def zipcode(self, zipcode):
        self.driver.find_element(By.ID, self.txtbox_zipcode_id).send_keys(zipcode)

    def phonenum(self, phonenum):
        self.driver.find_element(By.ID, self.txtbox_phonenum_id).send_keys(phonenum)

    def faxnum(self, faxnum):
        self.driver.find_element(By.ID, self.txtbox_faxnum_id).send_keys(faxnum)

    def continue_click(self):
        self.driver.find_element(By.XPATH, self.btn_continue_xpath).click()


# Payment method

    def payment_check_click(self):
        self.driver.find_element(By.XPATH, self.rb_check_xpath).click()

    def payment_creditcard_click(self):
        self.driver.find_element(By.XPATH, self.rb_creditcard_xpath).click()

    def continue4_click(self):
        self.driver.find_element(By.XPATH, self.btn_continue4_xpath).click()

# Payment method for credit card method

    def set_cardtype(self, cardtype):
        self.cardtype = Select(self.driver.find_element(By.XPATH,self.dpd_cardtype_xpath))
        self.cardtype.select_by_visible_text(cardtype)

    def cardholdername(self, cardholdername):
        self.driver.find_element(By.NAME, self.txtbox_cardholdername_name).send_keys(cardholdername)

    def cardnumber(self, cardnumber):
        self.driver.find_element(By.NAME, self.txtbox_cardnumber_name).send_keys(cardnumber)

    def set_expdate_month(self, expdate_month):
        self.expdate_month = Select(self.driver.find_element(By.XPATH,self.dpd_expdate_month_xpath))
        self.expdate_month.select_by_visible_text(expdate_month)

    def set_expdate_year(self, expdate_year):
        self.expdate_year = Select(self.driver.find_element(By.XPATH,self.dpd_expdate_year_xpath))
        self.expdate_year.select_by_visible_text(expdate_year)

    def cardcode(self, cardcode):
        self.driver.find_element(By.XPATH, self.txtbox_cardcode_xpath).send_keys(cardcode)

    def continue5_click(self):
        self.driver.find_element(By.XPATH, self.btn_continue5_xpath).click()

# Confirm order
    def confirm_click(self):
        self.driver.find_element(By.XPATH, self.btn_confirm_xpath).click()

    def getconfirmmsg(self):
        try:
            return self.driver.find_element(By.XPATH,self.text_order_processed_conf_xpath).text
        except:
            None

    def continue6_click(self):
        self.driver.find_element(By.XPATH, self.btn_continue6_xpath).click()

    def ordernb_get(self):
        try:
            return self.driver.find_element(By.XPATH, self.txt_ordernb_xpath).text
        except:
            None
