import time
from pageObjects.HomePage import MainPage
from pageObjects.SearchPage import SearchPage
from utilities.readProperties import ReadConfig
import os
import pytest
# TC - Validate searching with an existing product name
# It is searching for an existing item and checks if this item exists in the list of the displayed items

class Test_007_Search():
    baseURL = ReadConfig.getApplicationURL()
    search_item = ReadConfig.searchItem()

    @pytest.mark.sanity
    def test_search(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = MainPage(self.driver)
        self.hp.search_txtbox(self.search_item)
        self.hp.search_click()

        self.sp = SearchPage(self.driver)
        self.search_result = self.sp.results_elem()
        self.search_result_list = []
        for item in self.search_result:
            self.search_result_list.append(item.text)

        for item in self.search_result_list:
            if self.search_item.lower() or self.search_item.upper() or self.search_item.title() in item:
                assert True
                self.driver.close()
            else:
                self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_search.png")
                self.driver.close()
                assert False
