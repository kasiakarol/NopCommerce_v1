import os
import time
from pageObjects.HomePage import MainPage
from pageObjects.SearchPage import SearchPage
from pageObjects.ProdDisplayPage import ProdDisplayPage
from pageObjects.WishlistPage import WishlistPage
from utilities.readProperties import ReadConfig
import pytest

# TC_015 - Validate removing product from 'Wishlist' page
# It is adding 'wishlist_to_add' elements from config.ini to the wishlist using a for loop.
# Then by using dynamic xpath, it's deleting one product defined as 'wishlist_to_delete' object
# As a confirmation, it's checking if the deleted product doesn't exist in the Wishlist table.

class Test_012_WishList():
    baseURL = ReadConfig.getApplicationURL()
    search_item = ReadConfig.searchItem()
    wishlist_prod = ReadConfig.wishlist_to_add()
    wishlist_del_prod = ReadConfig.wishlist_to_delete()
    len_wishlist_prod = len(wishlist_prod)

    @pytest.mark.regression
    def test_wishlist(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = MainPage(self.driver)
        for p in range(0, len(self.wishlist_prod)):
            self.hp.search_txtbox(self.wishlist_prod[p])
            self.hp.search_click()
            self.sp = SearchPage(self.driver)
            self.sp.results_elem_click()
            self.pdp = ProdDisplayPage(self.driver)
            self.pdp.add_wishlist_click()
            self.pdp.home_page_click()
        self.hp.wishlist()

        self.wp = WishlistPage(self.driver)
        self.wp.delete_product()

        if self.wishlist_del_prod not in self.wp.wishlist_elements():
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_wishlist.png")
            self.driver.close()
            assert False

