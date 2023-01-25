from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class MyAccountDownloadProd():
    msg_noproducts_xpath = "//div[@class='no-data']"
    down_prod_list_xpath = "//td[@class='product']/a"

    # constructor:
    def __init__(self, driver):
        self.driver = driver

    def msg_no_products(self):
        try:
            return self.driver.find_element(By.XPATH,self.msg_noproducts_xpath).text
        except:
            None

    def down_prod_list_compl(self):
        down_prod_list = []
        down_prod = self.driver.find_elements(By.XPATH, self.down_prod_list_xpath)
        for prod in down_prod:
            down_prod_list.append(prod.text)
        return down_prod_list
