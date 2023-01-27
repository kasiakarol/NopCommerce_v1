from selenium import webdriver
from selenium.webdriver.common.by import By

class MyAccountRewardPoints():

    page_title_xpath = "//div[@class='page-title']/h1"

#constructor:
    def __init__(self,driver):
        self.driver=driver

    def page_title_text(self):
        try:
            return self.driver.find_element(By.XPATH, self.page_title_xpath).text
        except:
            None



