from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utilities.readProperties import ReadConfig

class ProdReviewPage():
    rating = ReadConfig.rating()
    txtbox_revtitle_id = "AddProductReview_Title"
    txtbox_revtext_id = "AddProductReview_ReviewText"
    rbtn_rating_xpath = "//input[@id='addproductrating_"+str(rating)+"']"
    btn_submit_review_name = "add-review"
    textmsg_rev_subm_xpath = "//div[@class='result' = 'Product review is successfully added.']"
    logo_homepage_xpath = "//img[@alt='nopCommerce demo store']"


#constructor:
    def __init__(self,driver):
        self.driver=driver

    def add_review_title(self, rev_title):
        self.driver.find_element(By.ID, self.txtbox_revtitle_id).send_keys(rev_title)

    def add_review_text(self, rev_text):
        self.driver.find_element(By.ID, self.txtbox_revtext_id).send_keys(rev_text)

    def add_rating(self):
        self.driver.find_element(By.XPATH, self.rbtn_rating_xpath).click()

    def submit_review(self):
        self.driver.find_element(By.NAME, self.btn_submit_review_name).click()

    def getreviewconfmsg(self):
        try:
            return self.driver.find_element(By.XPATH,self.textmsg_rev_subm_xpath).text
        except:
            None

    def logo_homepage_click(self):
        self.driver.find_element(By.XPATH, self.logo_homepage_xpath).click()