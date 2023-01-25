import time
from pageObjects.HomePage import MainPage
from pageObjects.SearchPage import SearchPage
from pageObjects.ProdDisplayPage import ProdDisplayPage
from utilities.readProperties import ReadConfig
import os
from selenium.webdriver.common.by import By
import pytest
# TC01 - Validate adding the product to Cart from 'Product Display' page

class Test_009_AddToCart():
    baseURL = ReadConfig.getApplicationURL()
    search_item = ReadConfig.searchItem()

    @pytest.mark.sanity
    def test_add_to_cart(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = MainPage(self.driver)
        self.hp.search_txtbox(self.search_item)
        self.hp.search_click()

        self.sp = SearchPage(self.driver)
        self.sp.result_click()

        self.pdp = ProdDisplayPage(self.driver)
        self.pdp.add_to_cart_click()
        self.pdp.addtocart_confmsg_click()
        time.sleep(3)

        self.elem = self.driver.find_element(By.LINK_TEXT, self.search_item)
        if self.elem.is_displayed():
            assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_AddToCart.png")
            assert False
        self.driver.close()

