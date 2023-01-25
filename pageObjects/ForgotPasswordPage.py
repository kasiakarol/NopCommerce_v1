from selenium import webdriver
from selenium.webdriver.common.by import By

class ForgPasswordPage():
    txtbox_insemail_id = "Email"
    button_recover_name = "send-email"
    bar_conf_xpath = "//p[@class='content' = 'Email with instructions has been sent to you.']"
    bar_conf_error_xpath = "//p[@class='content' = 'Email not found./']"

    def __init__(self,driver):
        self.driver=driver

    def forgpwdemail(self, email):
        self.driver.find_element(By.ID, self.txtbox_insemail_id).send_keys(email)

    def recover_click(self):
        self.driver.find_element(By.NAME, self.button_recover_name).click()

    def bar_conf(self):
        try:
            return self.driver.find_element(By.XPATH, self.bar_conf_xpath).text
        except:
            None

    def bar_conf_neg(self):
        try:
            return self.driver.find_element(By.XPATH, self.bar_conf_error_xpath).text
        except:
            None
