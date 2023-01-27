from pageObjects.HomePage import MainPage
from utilities.readProperties import ReadConfig
from pageObjects.ContactUsPage import ContactUs
import pytest
import os

# TC 006 - Validate submitting the 'Contact Us' form by proiding all the details.

class Test_027_ContactUs():
    baseURL = ReadConfig.getApplicationURL()
    name_contact = ReadConfig.name_contact()
    email_contact = ReadConfig.email_contact()
    enquiry_contact = ReadConfig.enquiry_contact()


    @pytest.mark.regression
    def test_contact_us(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = MainPage(self.driver)
        self.hp.contact_us_click()
        self.cu = ContactUs(self.driver)
        self.cu.contactus_name(self.name_contact)
        self.cu.contactus_email(self.email_contact)
        self.cu.contactus_enquiry(self.enquiry_contact)
        self.cu.contactus_submit()

        if self.cu.conf_msg() == "Your enquiry has been successfully sent to the store owner.":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "contact_us.png")
            self.driver.close()
            assert False


