import time
from pageObjects.HomePage import MainPage
from pageObjects.SearchPage import SearchPage
from utilities.readProperties import ReadConfig
import os
from pageObjects.CompareProdPage import CompareProdPage
import pytest

# TC_PC_013 - Validate the 'Compare Products' page when more than 2 products are added to the page for comparison
# It adds 3 products to Compare List page and validates if all requested products exist in product comparison table


class Test_008_CompareProd():
    baseURL = ReadConfig.getApplicationURL()
    compare_prod_item1 = ReadConfig.compareProd1()
    compare_prod_item2 = ReadConfig.compareProd2()
    compare_prod_item3 = ReadConfig.compareProd3()

    @pytest.mark.regression
    def test_compare_prod(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = MainPage(self.driver)
        self.hp.search_txtbox(self.compare_prod_item1)
        self.hp.search_click()

        self.sp = SearchPage(self.driver)
        self.sp.comp_prod()
        self.sp.search_txtbox(self.compare_prod_item2)
        self.sp.search_click()
        self.sp.comp_prod()
        self.sp.search_txtbox(self.compare_prod_item3)
        self.sp.search_click()
        self.sp.comp_prod()
        self.sp.compare_prod_link()

        self.cp = CompareProdPage(self.driver)
        self.cp.countColumnsComp()
        items = self.cp.rowsCompareProdName(self.cp.countColumnsComp())
        self.comprod_list = []
        for item in items:
            self.comprod_list.append(item.text)
        self.final_results = []

        if self.compare_prod_item1 and self.compare_prod_item2 and self.compare_prod_item3 in self.comprod_list:
            if len(self.comprod_list) == 3:
                assert True
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_prod_comp.png")
            assert False
        self.driver.close()
