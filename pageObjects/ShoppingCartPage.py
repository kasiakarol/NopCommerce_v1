from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ShoppingCartPage():
    txtbox_qty1_xpath = "//table//tr[1]/td[5]/input"
    btn_updatesc_xpath = "//button[@id='updatecart']"
    logo_homepage_xpath = "//img[@alt='nopCommerce demo store']"
    btn_checkout_id = "checkout"
    checkbox_termsconf_name = "termsofservice"
    text_total_xpath = "//tr[@class='order-total']//span[@class='value-summary']"

#constructor:
    def __init__(self,driver):
        self.driver=driver

    def quantity1_update(self, qty):
        self.driver.find_element(By.XPATH, self.txtbox_qty1_xpath).clear()
        self.driver.find_element(By.XPATH, self.txtbox_qty1_xpath).send_keys(qty)

    def update_shopcart_click(self):
        self.driver.find_element(By.XPATH, self.btn_updatesc_xpath).click()

    def get_quantity1(self):
        qty1 = self.driver.find_element(By.XPATH, self.txtbox_qty1_xpath).get_attribute("value")
        return qty1

    def logo_homepage_click(self):
        self.driver.find_element(By.XPATH, self.logo_homepage_xpath).click()

    def checkout_click(self):
        self.driver.find_element(By.ID, self.btn_checkout_id).click()

    def terms_conf_click(self):
        self.driver.find_element(By.NAME, self.checkbox_termsconf_name).click()

    def total_price(self):
        try:
            return self.driver.find_element(By.XPATH, self.text_total_xpath).text
        except:
            None