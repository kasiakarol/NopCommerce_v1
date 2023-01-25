from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

class MyAccountOrders():
    list_orders_xpath = "//strong[contains(.,'Order Number: ')]"
    btn_details1_xpath = "(//button[@type='button'][normalize-space()='Details'])[1]"

    # constructor:
    def __init__(self, driver):
        self.driver = driver

    def order_list(self):
        self.order_list = self.driver.find_elements(By.XPATH, self.list_orders_xpath)
        orders = []
        for order in self.order_list:
            orders.append(order.text)
        return orders

    def details1_click(self):
        self.driver.find_element(By.XPATH, self.btn_details1_xpath).click()