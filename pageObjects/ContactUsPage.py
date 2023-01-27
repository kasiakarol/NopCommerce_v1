from selenium.webdriver.common.by import By

class ContactUs():

    conf_msg_xpath = "//div[@class='result']"
    txtbox_name_id = "FullName"
    txtbox_email_id = "Email"
    txtbox_enquiry_id = "Enquiry"
    btn_submit_name = "send-email"

#constructor:
    def __init__(self,driver):
        self.driver=driver

    def conf_msg(self):
        try:
            return self.driver.find_element(By.XPATH, self.conf_msg_xpath).text
        except:
            None

    def contactus_name(self, name_contact):
        self.driver.find_element(By.ID, self.txtbox_name_id).send_keys(name_contact)

    def contactus_email(self, email_contact):
        self.driver.find_element(By.ID, self.txtbox_email_id).send_keys(email_contact)

    def contactus_enquiry(self, enquiry_contact):
        self.driver.find_element(By.ID, self.txtbox_enquiry_id).send_keys(enquiry_contact)

    def contactus_submit(self):
        self.driver.find_element(By.NAME, self.btn_submit_name).click()

