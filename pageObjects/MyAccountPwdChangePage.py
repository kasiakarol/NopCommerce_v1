from selenium import webdriver
from selenium.webdriver.common.by import By

class MyAccountPwdChange():

    txtbox_oldpwd_id = "OldPassword"
    txtbox_newpwd_id = "NewPassword"
    txtbox_confirmpwd_id = "ConfirmNewPassword"
    btn_changepwd_xpath = "//button[normalize-space()='Change password']"
    msg_pwdchangeerror_xpath = "//span[@id='ConfirmNewPassword-error']"

#constructor:
    def __init__(self,driver):
        self.driver=driver

    def old_pwd(self, old_pwd):
        self.driver.find_element(By.ID, self.txtbox_oldpwd_id).send_keys(old_pwd)

    def new_pwd(self, new_pwd):
        self.driver.find_element(By.ID, self.txtbox_newpwd_id).send_keys(new_pwd)

    def confirm_pwd(self, confirm_pwd):
        self.driver.find_element(By.ID, self.txtbox_confirmpwd_id).send_keys(confirm_pwd)

    def change_pwd_click(self):
        self.driver.find_element(By.XPATH, self.btn_changepwd_xpath).click()

    def msg_pwdchange_error_text(self):
        try:
            return self.driver.find_element(By.XPATH, self.msg_pwdchangeerror_xpath).text
        except:
            None
