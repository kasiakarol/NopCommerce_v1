import os
import time
from pageObjects.HomePage import MainPage
from pageObjects.SearchPage import SearchPage
from pageObjects.ShoppingCartPage import ShoppingCartPage
from pageObjects.ProdDisplayPage import ProdDisplayPage
from utilities.readProperties import ReadConfig
import pytest

# TC_008 - updating the quantity of in the shopping cart
# checking the functionality of adding the product to the shopping cart.
# then changing the quantity, clicking on update changes
# test case will check if the quantity of the product matches with the requested quantity

class Test_013_ShoppingCart():
    baseURL = ReadConfig.getApplicationURL()
    search_item = ReadConfig.searchItem()
    qty_to_set = ReadConfig.qty_to_set_shoppingcart()

    @pytest.mark.sanity
    def test_shoppingcart(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = MainPage(self.driver)
        self.hp.search_txtbox(self.search_item)
        self.hp.search_click()

        self.sp = SearchPage(self.driver)
        self.sp.results_elem_click()

        self.pdp = ProdDisplayPage(self.driver)
        self.pdp.add_to_cart_click()
        self.pdp.addtocart_confmsg_click()

        self.scp = ShoppingCartPage(self.driver)
        self.scp.quantity1_update(self.qty_to_set)
        self.scp.update_shopcart_click()
        self.driver.refresh()

        if self.scp.get_quantity1() == self.qty_to_set:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_qtyupdate.png")
            self.driver.close()
            assert False



