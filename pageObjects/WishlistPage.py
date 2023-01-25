from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import ReadConfig
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from testCases import conftest


class WishlistPage():
    rows = len(ReadConfig.wishlist_to_add())
    wishlist_to_delete = ReadConfig.wishlist_to_delete()
    count_rows_xpath = "//table[@class='cart']//tbody//tr"
    count_columns_xpath = "//table[@class='cart']//thead//tr[1]//th"

    def __init__(self, driver):
        self.driver = driver

    def rows_count(self):
        rows = self.driver.find_elements(By.XPATH, self.count_rows_xpath)
        return len(rows)

    def columns_count(self):
        columns = self.driver.find_elements(By.XPATH, self.count_columns_xpath)
        return len(columns)

    def delete_product(self):
        for r in range(1, self.rows):
            wishlist_products_xpath = "//table[@class='cart']//tbody/tr[" + str(r) + "]/td[4]"
            delete_the_product_xpath = "//table[@class='cart']//tbody/tr[" + str(r) + "]/td[8]"
            self.prodName = self.driver.find_element(By.XPATH, wishlist_products_xpath).text
            if self.prodName == self.wishlist_to_delete:
                self.driver.find_element(By.XPATH, delete_the_product_xpath).click()

    def wishlist_elements(self):
        wishlist_elem = []
        for r in range(1, self.rows):
            wishlist_products_xpath = "//table[@class='cart']//tbody/tr[" + str(r) + "]/td[4]"
            wishlist_elem.append(self.driver.find_element(By.XPATH, wishlist_products_xpath).text)
            return wishlist_elem

