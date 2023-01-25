from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProdDisplayPage():
    btn_addtocart_xpath = "//button[contains(@id,'add-to-cart-button')]"
    link_msg_addtocart_xpath = "//a[normalize-space()='shopping cart']"
    txt_title_xpath = "//div[@class='product-name']/h1"
    txt_prodcode_xpath = "//div[@class='sku']/span[2]"
    img_mainpic_xpath = "//div[@class='picture']/a/img"
    link_addreview_linktxt = "Add your review"
    btn_addtowishlist_xpath = "//button[contains(@id,'add-to-wishlist-button')]"
    link_msg_addtowishlist_xpath = "//a[normalize-space()='wishlist']"
    logo_homepage_xpath = "//img[@alt='nopCommerce demo store']"


#constructor:
    def __init__(self,driver):
        self.driver=driver

    def add_to_cart_click(self):
        self.driver.find_element(By.XPATH, self.btn_addtocart_xpath).click()

    def addtocart_confmsg_click(self):
        self.wait = WebDriverWait(self.driver, 5)
        self.element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.link_msg_addtocart_xpath)))
        self.element.click()

    def title_capture(self):
        title = self.driver.find_element(By.XPATH, self.txt_title_xpath).text
        return title

    def prod_code(self):
        return self.driver.find_element(By.XPATH, self.txt_prodcode_xpath)

    def img_main(self):
        return self.driver.find_element(By.XPATH, self.img_mainpic_xpath)

    def img_main_click(self):
        self.driver.find_element(By.XPATH, self.img_mainpic_xpath).click()

    def add_review_click(self):
        self.driver.find_element(By.LINK_TEXT, self.link_addreview_linktxt).click()

    def add_wishlist_click(self):
        self.driver.find_element(By.XPATH, self.btn_addtowishlist_xpath).click()

    def addtowishlist_confmsg_click(self):
        self.wait = WebDriverWait(self.driver, 5)
        self.element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.link_msg_addtowishlist_xpath)))
        self.element.click()

    def home_page_click(self):
        self.driver.find_element(By.XPATH, self.logo_homepage_xpath).click()

