from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class MainPage():
#locators:
    link_register_linktext = "Register"
    link_login_linktext = "Log in"
    link_wishlist_linktext = "Wishlist"
    link_shoppingcart_linktext = "Shopping cart"
    txtbox_search_id = "small-searchterms"
    button_search_xpath = "//button[@class='button-1 search-box-button']"
    link_logout_linktext = "Log out"
    logo_homepage_xpath = "//img[@alt='nopCommerce demo store']"
    confmsg_welcome_xpath = "//h2[normalize-space()='Welcome to our store']"
    catpage_electr_xpath = "//ul[@class='top-menu notmobile']//a[normalize-space()='Electronics']"
    catpage_cellphones_xpath = "//ul[@class='top-menu notmobile']//a[normalize-space()='Cell phones']"
    link_news_xpath = "//a[normalize-space()='News']"
    link_myaccount_linktext = "My account"
    catpage_digitaldownl_xpath = "//ul[@class='top-menu notmobile']//a[normalize-space()='Digital downloads']"


#constructor:
    def __init__(self,driver):
        self.driver=driver

#action methods:
    def register(self):
        self.driver.find_element(By.LINK_TEXT, self.link_register_linktext).click()

    def login(self):
        self.driver.find_element(By.LINK_TEXT, self.link_login_linktext).click()

    def wishlist(self):
        self.driver.find_element(By.LINK_TEXT, self.link_wishlist_linktext).click()

    def shoppingcart(self):
        self.driver.find_element(By.LINK_TEXT, self.link_shoppingcart_linktext).click()

    def search_txtbox(self, search_txt):
        self.driver.find_element(By.ID, self.txtbox_search_id).send_keys(search_txt)

    def search_click(self):
        self.driver.find_element(By.XPATH, self.button_search_xpath).click()

    def logout_click(self):
        self.driver.find_element(By.LINK_TEXT, self.link_logout_linktext).click()

    def logo_homepage_click(self):
        self.driver.find_element(By.XPATH, self.logo_homepage_xpath).click()

    def conf_message_text(self):
        try:
            return self.driver.find_element(By.XPATH, self.confmsg_welcome_xpath).text
        except:
            None

    def catpage_cellphones(self):
        electronics = self.driver.find_element(By.XPATH, self.catpage_electr_xpath)
        cellphones = self.driver.find_element(By.XPATH, self.catpage_cellphones_xpath)
        # mousehover
        act = ActionChains(self.driver)
        act.move_to_element(electronics).move_to_element(cellphones).click().perform()

    def news_click(self):
        self.driver.find_element(By.XPATH, self.news_click()).click()

    def myaccount_click(self):
        self.driver.find_element(By.LINK_TEXT, self.link_myaccount_linktext).click()

    def catpage_digital_downloads(self):
        self.driver.find_element(By.XPATH, self.catpage_digitaldownl_xpath).click()


