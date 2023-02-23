import os
import time
from pageObjects.HomePage import MainPage
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchPage import SearchPage
from pageObjects.ProdDisplayPage import ProdDisplayPage
from pageObjects.ProdReviewPage import ProdReviewPage
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from utilities.readProperties import ReadConfig
import pytest
from utilities import randomeString

# TC_PDP_008 - Validate the user is able to write a review for the product from the 'Add your review' tab of Product Display Page

# It takes 'search_item' product, and tries to add a review. It can be only added by a registered user it logs the user in
# The review is added, by filling in 'title' and 'text' text boxes and by choosing 'rating' radio button.
# After the review is submitted, the test validates if the confirmation message is correct

# Pre-requisites - user is registered - part of the test case.
class Test_011_ProdDisplayAddReview():
    baseURL = ReadConfig.getApplicationURL()
    search_item = ReadConfig.searchItem()
    password = ReadConfig.getPassword()
    rev_title = ReadConfig.revTitle()
    rev_text = ReadConfig.revText()
    rating = ReadConfig.rating()
    fname_reg = ReadConfig.fname_reg()
    lname_reg = ReadConfig.lname_reg()
    email = randomeString.random_login_generator() + '@test.com'

    @pytest.mark.regression
    def test_disp_prod_add_review(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = MainPage(self.driver)
        self.hp.register()
        self.rp = AccountRegistrationPage(self.driver)

        self.rp.setFirstName(self.fname_reg)
        self.rp.setLastName(self.lname_reg)
        self.rp.setEmail(self.email)
        self.rp.setPassword(self.password)
        self.rp.setConfirmPassword(self.password)
        self.rp.clickRegister()

        self.hp.search_txtbox(self.search_item)
        self.hp.search_click()

        self.sp = SearchPage(self.driver)
        self.sp.result_click()

        self.pdp = ProdDisplayPage(self.driver)
        self.pdp.add_review_click()

        self.hp.login()
        self.lp = LoginPage(self.driver)
        self.lp.insertEmail(self.email)
        self.lp.insertPassword(self.password)
        self.lp.logIn()

        self.prp = ProdReviewPage(self.driver)
        self.prp.add_review_title(self.rev_title)
        self.prp.add_review_text(self.rev_text)
        self.prp.add_rating()
        time.sleep(2)
        self.prp.submit_review()

        if self.prp.getreviewconfmsg() == "Product review is successfully added.":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_ReviewProdDisp.png")
            self.driver.close()
            assert False

