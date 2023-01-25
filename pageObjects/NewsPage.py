from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class NewsPage():
    logo_homepage_xpath = "//img[@alt='nopCommerce demo store']"

    def __init__(self,driver):
        self.driver=driver

    def logo_homepage_click(self):
        self.driver.find_element(By.XPATH, self.logo_homepage_xpath).click()

