from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AccountRegistrationPage():
    rb_male_id = "gender-male"
    rb_female_id = "gender-female"
    txt_firstname_name = "FirstName" #ok
    txt_lastname_name = "LastName" #ok
    dpd_dobday_name = "DateOfBirthDay"
    dpd_dobmonth_name = "DateOfBirthMonth"
    dpd_dobyear_name = "DateOfBirthYear"
    txt_email_name = "Email"
    txt_companyname_name = "Company"
    chk_newsletter_name = "Newsletter"
    txt_password_name = "Password"
    txt_confpassword_name = "ConfirmPassword"
    btn_register_name = "register-button"
    text_msg_compl_xpath = "//div[@class='result' = 'Your registration completed']"


    def __init__(self, driver):
        self.driver = driver

    def setGenderFemale(self):
        self.driver.find_element(By.ID, self.rb_female_id).click()

    def setGenderMale(self):
        self.driver.find_element(By.ID, self.rb_male_id).click()

    def setFirstName(self, fname):
        self.driver.find_element(By.NAME,self.txt_firstname_name).send_keys(fname)

    def setLastName(self, lname):
        self.driver.find_element(By.NAME,self.txt_lastname_name).send_keys(lname)

    def setDoBDay(self, day):
        self.day = Select(self.driver.find_element(By.NAME,self.dpd_dobday_name))
        self.day.select_by_value(day)

    def setDoBMonth(self, month):
        self.month = Select(self.driver.find_element(By.NAME,self.dpd_dobmonth_name))
        self.month.select_by_visible_text(month)

    def setDoBYear(self, year):
        self.year = Select(self.driver.find_element(By.NAME,self.dpd_dobyear_name))
        self.year.select_by_value(year)

    def setEmail(self, email):
        self.driver.find_element(By.NAME,self.txt_email_name).send_keys(email)

    def setCompanyName(self, cname):
        self.driver.find_element(By.NAME,self.txt_companyname_name).send_keys(cname)

    def setNewsletter(self):
        self.driver.find_element(By.NAME,self.chk_newsletter_name).click()

    def setPassword(self, pwd):
        self.driver.find_element(By.NAME,self.txt_password_name).send_keys(pwd)

    def setConfirmPassword(self, cnfpwd):
        self.driver.find_element(By.NAME,self.txt_confpassword_name).send_keys(cnfpwd)

    def clickRegister(self):
        self.driver.find_element(By.NAME,self.btn_register_name).click()

    def getcompletedmsg(self):
        try:
            return self.driver.find_element(By.XPATH,self.text_msg_compl_xpath).text
        except:
            None

