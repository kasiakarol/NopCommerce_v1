from pageObjects.ShoppingCartPage import ShoppingCartPage
import pytest
import os
from pageObjects.HomePage import MainPage
from pageObjects.SearchPage import SearchPage
from pageObjects.ProdDisplayPage import ProdDisplayPage
from pageObjects.NewsPage import NewsPage
from utilities.readProperties import ReadConfig

# TC_HP_003 - Validate navigating to Home Page from any page of the application using logo.

# verified for Search page, Shopping Cart, Product Display page, News Page

class Test_014_HomePage():
    baseURL = ReadConfig.getApplicationURL()
    search_item = ReadConfig.searchItem()

    @pytest.mark.regression
    def test_homepage(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = MainPage(self.driver)
        self.hp.search_txtbox(self.search_item)
        self.hp.search_click()

        results=[]
        self.sp = SearchPage(self.driver)
        self.sp.logo_homepage_click()

        if self.hp.conf_message_text() == "Welcome to our store":
            results.append("yes")
        else:
            results.append("no")

        self.hp.shoppingcart()
        self.sc = ShoppingCartPage(self.driver)
        self.sc.logo_homepage_click()

        if self.hp.conf_message_text() == "Welcome to our store":
            results.append("yes")
        else:
            results.append("no")

        self.hp = MainPage(self.driver)
        self.hp.search_txtbox(self.search_item)
        self.hp.search_click()
        self.pdp = ProdDisplayPage(self.driver)
        self.pdp.img_main_click()
        self.pdp.home_page_click()

        if self.hp.conf_message_text() == "Welcome to our store":
            results.append("yes")
        else:
            results.append("no")

        self.hp.catpage_cellphones()
        self.sp.logo_homepage_click()

        if self.hp.conf_message_text() == "Welcome to our store":
            results.append("yes")
        else:
            results.append("no")

        self.np = NewsPage(self.driver)
        self.np.logo_homepage_click()

        if self.hp.conf_message_text() == "Welcome to our store":
            results.append("yes")
        else:
            results.append("no")

        # final validation
        if "no" not in results:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_homepage_logo.png")
            self.driver.close()
            assert False


