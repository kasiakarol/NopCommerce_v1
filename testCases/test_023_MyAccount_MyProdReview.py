from pageObjects.HomePage import MainPage
from pageObjects.LoginPage import LoginPage
from pageObjects.MyAccountCustInfo import MyAccountCustInfo
from pageObjects.AccountRegistrationPage import AccountRegistrationPage
from pageObjects.ProdReviewPage import ProdReviewPage
from pageObjects.SearchPage import SearchPage
from pageObjects.ProdDisplayPage import ProdDisplayPage
from pageObjects.MyAccountReviews import MyAccountReviews
from utilities.readProperties import ReadConfig
import pytest
from utilities import randomeString
import os
import time


# TC - validate My Account > 'My product reviews' page, when the user added a review of the product
# It checks title, text and rating of the review

# Pre-requisites - user is registered - part of the test case.

class Test_023_MyAccountMyProdReview():
    baseURL = ReadConfig.getApplicationURL()
    password = ReadConfig.getPassword()
    fname_reg = ReadConfig.fname_reg()
    lname_reg = ReadConfig.lname_reg()
    email = randomeString.random_login_generator() + '@test.com'
    search_item = ReadConfig.searchItem()
    rev_title = ReadConfig.revTitle()
    rev_text = ReadConfig.revText()
    rating = ReadConfig.rating()

    @pytest.mark.myaccount
    def test_my_prod_review(self, setup):
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

        self.hp = MainPage(self.driver)

        self.hp.register()
        self.rp = AccountRegistrationPage(self.driver)

        self.rp.setFirstName(self.fname_reg)
        self.rp.setLastName(self.lname_reg)
        self.email = randomeString.random_login_generator()+'@test.com'
        self.rp.setEmail(self.email)
        self.rp.setPassword(self.password)
        self.rp.setConfirmPassword(self.password)
        self.rp.clickRegister()

        self.hp.login()
        self.lp = LoginPage(self.driver)
        self.lp.insertEmail(self.email)
        self.lp.insertPassword(self.password)
        self.lp.logIn()

        self.hp.search_txtbox(self.search_item)
        self.hp.search_click()

        self.sp = SearchPage(self.driver)
        self.sp.result_click()

        self.pdp = ProdDisplayPage(self.driver)
        self.pdp.add_review_click()

        self.prp = ProdReviewPage(self.driver)
        self.prp.add_review_title(self.rev_title)
        self.prp.add_review_text(self.rev_text)
        self.prp.add_rating()
        time.sleep(2)
        self.prp.submit_review()

        self.hp.myaccount_click()
        self.myci = MyAccountCustInfo(self.driver)
        self.myci.reviews_click()

        self.mypr = MyAccountReviews(self.driver)

        results = []
        if self.mypr.msg_review_for() == self.search_item:
            results.append("yes")
        else:
            results.append("no")

        if self.mypr.msg_review_title() == self.rev_title:
            results.append("yes")
        else:
            results.append("no")

        if self.mypr.msg_review_text() == self.rev_text:
            results.append("yes")
        else:
            results.append("no")

        if self.mypr.rating_info() == "width: 100%;" and self.rating == "5":
            results.append("yes")
        elif self.mypr.rating_info() == "width: 80%;" and self.rating == "4":
            results.append("yes")
        elif self.mypr.rating_info() == "width: 60%;" and self.rating == "3":
            results.append("yes")
        elif self.mypr.rating_info() == "width: 40%;" and self.rating == "2":
            results.append("yes")
        elif self.mypr.rating_info() == "width: 20%;" and self.rating == "1":
            results.append("yes")
        else:
            results.append("no")

        # final validation
        if "no" not in results:
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(os.path.abspath(os.curdir) + "\\screenshots\\" + "test_myaccount_review.png")
            self.driver.close()
            assert False