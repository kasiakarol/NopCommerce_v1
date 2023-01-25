from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class CompareProdPage():
    columns_compare_xpath = "//tbody/tr[1]/td"
    rows_compare_xpath = '//tbody/tr[3]/td["+str(r)+"]'
    logo_homepage_xpath = "//img[@alt='nopCommerce demo store']"

    def __init__(self, driver):
        self.driver = driver

    def countColumnsComp(self):
        columns = self.driver.find_elements(By.XPATH,self.columns_compare_xpath)
        return len(columns)-1

    def rowsCompareProdName(self, rows):
        for r in range(2, CompareProdPage.countColumnsComp(self)+1):
            comp_prod = self.driver.find_elements(By.XPATH, self.rows_compare_xpath)
            return comp_prod[1:]

    def logo_homepage_click(self):
        self.driver.find_element(By.XPATH, self.logo_homepage_xpath).click()


