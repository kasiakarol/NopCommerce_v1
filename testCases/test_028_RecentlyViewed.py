import os
import time
from pageObjects.HomePage import MainPage
from pageObjects.SearchPage import SearchPage
from pageObjects.ProdDisplayPage import ProdDisplayPage
from pageObjects.RecentlyViewed import RecentlyViewedPage
from utilities.readProperties import ReadConfig
import pytest

# TC_015 - Validate 'Recently Viewed Products' page


class Test_028_RecentlyViewed():
    baseURL = ReadConfig.getApplicationURL()
    recently_viewed = ReadConfig.recently_viewed()

    @pytest.mark.regression
    def test_recently_viewed(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = MainPage(self.driver)
        for p in range(0, len(self.recently_viewed)):
            self.hp.search_txtbox(self.recently_viewed[p])
            self.hp.search_click()
            self.sp = SearchPage(self.driver)
            self.sp.results_elem_click()
            self.pdp = ProdDisplayPage(self.driver)
            self.pdp.home_page_click()

        self.hp.recently_viewed_click()
        self.rv = RecentlyViewedPage(self.driver)

        if self.rv.recently_viewed_list() == self.recently_viewed[::-1]:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "recently_viewed.png")
            self.driver.close()
            assert False



