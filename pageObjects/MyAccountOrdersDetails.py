from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class MyAccountOrdersDetails():
    btn_print_pdf_invoice_xpath = "//a[normalize-space()='PDF Invoice']"
    msg_orderinf_xpath = "//div[@class='page-title']/h1"

    # constructor:
    def __init__(self, driver):
        self.driver = driver

    def print_invoice_click(self):
        self.driver.find_element(By.XPATH, self.btn_print_pdf_invoice_xpath).click()

    def order_inf_msg(self):
        try:
            return self.driver.find_element(By.XPATH,self.msg_orderinf_xpath).text
        except:
            None