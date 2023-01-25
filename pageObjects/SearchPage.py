from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SearchPage():
    link_results_xpath = "//div[@class='item-grid']//h2[@class='product-title']"
    btn_compare_xpath = "//button[normalize-space()='Add to compare list']"
    txtbox_search_id = "small-searchterms"
    button_search_xpath = "//button[@class='button-1 search-box-button']"
    link_compprod_xpath = "//a[normalize-space()='product comparison']"
    link_result_xpath = "//div[@class = 'product-item']//h2[@class='product-title']/a"
    btn_wishlist_xpath = "//button[normalize-space()='Add to wishlist']"
    logo_homepage_xpath = "//img[@alt='nopCommerce demo store']"
    btn_shoppingcart_xpath = "//span[@class='cart-label']"

# downloadable products
    link_products_xpath = "//h2/a"

#constructor:
    def __init__(self,driver):
        self.driver=driver

    def results_elem(self):
        elem_found = self.driver.find_elements(By.XPATH, self.link_results_xpath)
        for self.item in elem_found:
            return elem_found

    def results_elem_click(self):
        self.driver.find_element(By.XPATH, self.link_result_xpath).click()

    def comp_prod(self):
        self.driver.find_element(By.XPATH, self.btn_compare_xpath).click()

    def search_txtbox(self, search_txt):
        self.driver.find_element(By.ID, self.txtbox_search_id).send_keys(search_txt)

    def search_click(self):
        self.driver.find_element(By.XPATH, self.button_search_xpath).click()

    def compare_prod_link(self):
        self.wait = WebDriverWait(self.driver, 5)
        self.element = self.wait.until(
            EC.visibility_of_element_located((By.XPATH, self.link_compprod_xpath)))
        self.element.click()

    def result_click(self):
        self.driver.find_element(By.XPATH, self.link_result_xpath).click()

    def add_wishlist(self):
        self.driver.find_element(By.XPATH, self.btn_wishlist_xpath).click()

    def logo_homepage_click(self):
        self.driver.find_element(By.XPATH, self.logo_homepage_xpath).click()

# downloadable products

    def add_to_shopcart_all_prod(self):
        products = self.driver.find_elements(By.XPATH, self.link_products_xpath)
        prod_titles = []
        for prod in products:
             prod_titles.append(prod.text)
        return prod_titles

    def shopping_cart_click(self):
        self.driver.find_element(By.XPATH, self.btn_shoppingcart_xpath).click()