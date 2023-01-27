from selenium.webdriver.common.by import By


class RecentlyViewedPage():
    list_recently_viewed_xpath = "//h2[@class='product-title']//a"

    def __init__(self, driver):
        self.driver = driver

    def recently_viewed_list(self):
        rec_viewed_list = []
        rec_viewed = self.driver.find_elements(By.XPATH, self.list_recently_viewed_xpath)
        for prod in rec_viewed:
            rec_viewed_list.append(prod.text)
        return rec_viewed_list
