from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class MyAccountBackInStock():

    text_pageheading_xpath = "//h1[normalize-space()='My account - Back in stock subscriptions']"
    conf_msg_no_data_xpath = "//div[@class='no-data']"
    page_title_xpath = "//div[@class='page-title']/h1"

#constructor:
    def __init__(self,driver):
        self.driver=driver

    def page_heading_text(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_pageheading_xpath).text
        except:
            None

    def msg_nodata_text(self):
        try:
            return self.driver.find_element(By.XPATH,self.conf_msg_no_data_xpath).text
        except:
            None

    def page_title_text(self):
        try:
            return self.driver.find_element(By.XPATH, self.page_title_xpath).text
        except:
            None



