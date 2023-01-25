from selenium.webdriver.common.by import By


class LoginPage():
    txt_email_id = "Email"
    txt_password_id = "Password"
    btn_login_xpath = "//button[normalize-space()='Log in']"
    rb_rememberme_name = 'RememberMe'
    link_forgotpwd_xpath = "//a[normalize-space()='Forgot password?']"
    link_myaccount_xpath = "//a[@class='ico-account']"
    link_logout_xpath = "//a[normalize-space()='Log out']"
    msg_login_error_xpath = "//div[@class='message-error validation-summary-errors']"

    def __init__(self, driver):
        self.driver = driver

    def insertEmail(self, email):
        self.driver.find_element(By.ID, self.txt_email_id).send_keys(email)

    def insertPassword(self, pwd):
        self.driver.find_element(By.ID, self.txt_password_id).send_keys(pwd)

    def logIn(self):
        self.driver.find_element(By.XPATH, self.btn_login_xpath).click()

    def rememberMe(self):
        self.driver.find_element(By.NAME,self.rb_rememberme_name).click()

    def forgotPsw(self):
        self.driver.find_element(By.XPATH, self.link_forgotpwd_xpath).click()

    def myaccount(self):
        try:
            return self.driver.find_element(By.XPATH, self.link_myaccount_xpath).is_displayed()
        except:
            None

    def logOut(self):
        self.driver.find_element(By.XPATH, self.link_logout_xpath).click()

    def error_msg(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_login_error_xpath).text
        except:
            None