import time
from pageObjects.HomePage import MainPage
from pageObjects.SearchPage import SearchPage
from pageObjects.ProdDisplayPage import ProdDisplayPage
from pageObjects.ShoppingCartPage import ShoppingCartPage
from utilities.readProperties import ReadConfig
import os
from selenium.webdriver.common.by import By
import pytest
# TC_CR_001 - Validate the complete functionality of the application by selecting 'EUR' currency - 'Add to cart' func.

class Test_025_AddToCartEUR():
    baseURL = ReadConfig.getApplicationURL()
    search_item = ReadConfig.searchItem()
    ccy = ReadConfig.ccy()

    @pytest.mark.sanity
    def test_add_to_cart_EUR(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = MainPage(self.driver)
        self.hp.change_currency(self.ccy)
        self.hp.search_txtbox(self.search_item)
        self.hp.search_click()

        self.sp = SearchPage(self.driver)
        self.sp.result_click()

        self.pdp = ProdDisplayPage(self.driver)
        self.pdp.add_to_cart_click()
        self.pdp.addtocart_confmsg_click()
        time.sleep(3)

        self.scp = ShoppingCartPage(self.driver)
        results=[]

        total = self.scp.total_price()
        if total[0] == "€":
            results.append("yes")
        else:
            results.append("no")

        self.elem = self.driver.find_element(By.LINK_TEXT, self.search_item)
        if self.elem.is_displayed():
            results.append("yes")
        else:
            results.append("no")

        # final validation
        if "no" not in results:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_addtocartEUR.png")
            self.driver.close()
            assert False

