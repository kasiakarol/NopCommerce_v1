import os
import time
from pageObjects.HomePage import MainPage
from pageObjects.SearchPage import SearchPage
from pageObjects.ProdDisplayPage import ProdDisplayPage
from utilities.readProperties import ReadConfig
import pytest

# TC_PDP_001 - Validate that product name, product code and main picture are displayed on the Product Display page
# It also saves a screenshot of the product's main picture


class Test_010_ProdDisplay():
    baseURL = ReadConfig.getApplicationURL()
    search_item = ReadConfig.searchItem()

    @pytest.mark.sanity
    def test_prod_display(self, setup):
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

        results = []
        # to check if the title is matching the searched product
        if self.search_item in self.pdp.title_capture():
            results.append("yes")
        else:
            results.append("no")

        # to check if product code is displayed
        if self.pdp.prod_code().is_displayed():
            results.append("yes")
        else:
            results.append("no")

        # to check if the picture exists and taking a screenshot of the first one
        if self.pdp.img_main().is_displayed():
            results.append("yes")
        else:
            results.append("no")

        self.pdp.img_main_click()
        time.sleep(3)
        self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_ProdDisplay.png")
        self.driver.close()

        #final validation
        if "no" not in results:
            assert True
        else:
            assert False
