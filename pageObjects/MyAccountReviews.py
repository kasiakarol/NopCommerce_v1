from selenium import webdriver
from selenium.webdriver.common.by import By

class MyAccountReviews():

    txtbox_oldpwd_id = "OldPassword"
    link_prodreview_xpath = "//span[@class='user']/a"
    text_reviewtitle_xpath = "//div[@class='review-title']"
    text_review_desc_xpath = "//div[@class='review-text']"
    rating_xpath = "//div[@class='rating']//div"

#constructor:
    def __init__(self,driver):
        self.driver=driver

    def old_pwd(self, old_pwd):
        self.driver.find_element(By.ID, self.txtbox_oldpwd_id).send_keys(old_pwd)

    def msg_review_for(self):
        try:
            return self.driver.find_element(By.XPATH,self.link_prodreview_xpath).text
        except:
            None

    def msg_review_title(self):
        try:
            return self.driver.find_element(By.XPATH,self.text_reviewtitle_xpath).text
        except:
            None

    def msg_review_text(self):
        try:
            return self.driver.find_element(By.XPATH,self.text_review_desc_xpath).text
        except:
            None

    def rating_info(self):
        rating_width = self.driver.find_element(By.XPATH,self.rating_xpath).get_attribute("style")
        return rating_width

