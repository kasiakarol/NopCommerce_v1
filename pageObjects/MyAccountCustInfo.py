from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class MyAccountCustInfo():

    text_pageheading_xpath = "//div[@class='page account-page customer-info-page']//h1"
    link_changepwd_xpath = "//a[normalize-space()='Change password']"
    link_addresses_xpath = "//li[@class='customer-addresses inactive']//a[normalize-space()='Addresses']"
    link_orders_xpath = "//li[@class='customer-orders inactive']//a[normalize-space()='Orders']"
    link_downloadableprod_xpath = "//a[normalize-space()='Downloadable products']"
    link_backinstock_xpath = "//a[normalize-space()='Back in stock subscriptions']"


#constructor:
    def __init__(self,driver):
        self.driver=driver

    def page_heading_text(self):
        return self.driver.find_element(By.XPATH, self.text_pageheading_xpath).text

    def pwd_change_click(self):
        self.driver.find_element(By.XPATH, self.link_changepwd_xpath).click()

    def addresses_click(self):
        self.driver.find_element(By.XPATH, self.link_addresses_xpath).click()

    def orders_click(self):
        self.driver.find_element(By.XPATH, self.link_orders_xpath).click()

    def download_prod_click(self):
        self.driver.find_element(By.XPATH, self.link_downloadableprod_xpath).click()

    def back_in_stock_click(self):
        self.driver.find_element(By.XPATH, self.link_backinstock_xpath).click()

