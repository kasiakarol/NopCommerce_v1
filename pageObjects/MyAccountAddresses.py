from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class MyAccountAddresses():
    text_name_xpath = "//li[@class='name']"
    text_email_xpath = "//li[@class='email']"
    text_phone_xpath = "//li[@class='phone']"
    text_fax_xpath = "//label[normalize-space()='Fax number:']"
    text_address1_xpath = "//li[@class='address1']"
    text_cityzip_xpath = "//li[@class='city-state-zip']"
    text_country_xpath = "//li[@class='country']"
    text_noaddresses_xpath = "//div[@class='no-data']"
    logo_homepage_xpath = "//img[@alt='nopCommerce demo store']"
    btn_deleteaddress_xpath = "//div//button[contains(.,'Delete')]"

    # constructor:
    def __init__(self, driver):
        self.driver = driver

    def addresses_name_text(self):
        return self.driver.find_element(By.XPATH, self.text_name_xpath).text

    def addresses_email_text(self):
        return self.driver.find_element(By.XPATH, self.text_email_xpath).text

    def addresses_phone_text(self):
        return self.driver.find_element(By.XPATH, self.text_phone_xpath).text

    def addresses_fax_text(self):
        return self.driver.find_element(By.XPATH, self.text_fax_xpath).text

    def addresses_address1_text(self):
        return self.driver.find_element(By.XPATH, self.text_address1_xpath).text

    def addresses_cityzip_text(self):
        return self.driver.find_element(By.XPATH, self.text_cityzip_xpath).text

    def addresses_country_text(self):
        return self.driver.find_element(By.XPATH, self.text_country_xpath).text

    def no_addresses_conf(self):
        return self.driver.find_element(By.XPATH, self.text_noaddresses_xpath).is_displayed()

    def home_page_click(self):
        self.driver.find_element(By.XPATH, self.logo_homepage_xpath).click()

    def delete_address_click(self):
        self.num_addresses = self.driver.find_elements(By.XPATH, "//ul[@class='info']")
        if len(self.num_addresses) >=1:
            for r in range(1, len(self.num_addresses)+1):
                self.driver.find_element(By.XPATH, "(//button[@type='button'][normalize-space()='Delete'])[1]").click()
                time.sleep(1)
                self.alertlog = self.driver.switch_to.alert
                time.sleep(1)
                self.alertlog.accept()
                time.sleep(1)


