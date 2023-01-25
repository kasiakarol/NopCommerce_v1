import configparser #needed to read the data from ini file
import os


config = configparser.RawConfigParser()
config.read("C:\\Users\\kasia\\PycharmProjects\\NopCommerce_v1\\configurations\\config.ini")

#one method for each variable
class ReadConfig():

    @staticmethod #we can directly call it by class, no need to create an object
    def getApplicationURL():
        #commonInfo - section name
        #baseURL - getting the value from config file
        url=(config.get('commonInfo', 'baseURL'))
        return url

    @staticmethod
    def getUseremail():
        username=(config.get('commonInfo', 'email'))
        return username

    @staticmethod
    def getPassword():
        password=(config.get('commonInfo', 'password'))
        return password

    @staticmethod
    def getUserEmailNeg():
        user_neg=(config.get('commonInfo', 'email_neg'))
        return user_neg

    @staticmethod
    def fname_reg():
        fname_reg=(config.get('commonInfo', 'fname_reg'))
        return fname_reg

    @staticmethod
    def lname_reg():
        lname_reg=(config.get('commonInfo', 'lname_reg'))
        return lname_reg

    @staticmethod
    def dob_day_reg():
        dob_day_reg=(config.get('commonInfo', 'dob_day_reg'))
        return dob_day_reg

    @staticmethod
    def dob_month_reg():
        dob_month_reg=(config.get('commonInfo', 'dob_month_reg'))
        return dob_month_reg

    @staticmethod
    def dob_year_reg():
        dob_year_reg=(config.get('commonInfo', 'dob_year_reg'))
        return dob_year_reg

    @staticmethod
    def company_name_reg():
        company_name_reg=(config.get('commonInfo', 'company_name_reg'))
        return company_name_reg

    @staticmethod
    def searchItem():
        search_item = (config.get('commonInfo', 'search_item'))
        return search_item

    @staticmethod
    def compareProd1():
        comp_prod1 = (config.get('commonInfo', 'compare_prod_item1'))
        return comp_prod1

    @staticmethod
    def compareProd2():
        comp_prod2 = (config.get('commonInfo', 'compare_prod_item2'))
        return comp_prod2

    @staticmethod
    def compareProd3():
        comp_prod3 = (config.get('commonInfo', 'compare_prod_item3'))
        return comp_prod3

    @staticmethod
    def revTitle():
        rev_title = (config.get('commonInfo', 'rev_title'))
        return rev_title

    @staticmethod
    def revText():
        rev_text = (config.get('commonInfo', 'rev_text'))
        return rev_text

    @staticmethod
    def rating():
        rating = (config.get('commonInfo', 'rating'))
        return rating

    @staticmethod
    def wishlist_to_add():
        wishlist_to_add = (config.get('commonInfo', 'wishlist_to_add'))
        items_list = wishlist_to_add.split(",\n")
        return items_list

    @staticmethod
    def wishlist_to_delete():
        wishlist_to_delete = (config.get('commonInfo', 'wishlist_to_delete'))
        return wishlist_to_delete

    @staticmethod
    def qty_to_set_shoppingcart():
        qty_to_set_shoppingcart = (config.get('commonInfo', 'qty'))
        return qty_to_set_shoppingcart

# Billing information

    @staticmethod
    def fname():
        fname = (config.get('commonInfo', 'fname'))
        return fname

    @staticmethod
    def lname():
        lname = (config.get('commonInfo', 'lname'))
        return lname

    @staticmethod
    def email_checkout():
        email_checkout = (config.get('commonInfo', 'email_checkout'))
        return email_checkout

    @staticmethod
    def country():
        country = (config.get('commonInfo', 'country'))
        return country

    @staticmethod
    def city():
        city = (config.get('commonInfo', 'city'))
        return city

    @staticmethod
    def address1():
        address1 = (config.get('commonInfo', 'address1'))
        return address1

    @staticmethod
    def set_address2():
        address2 = (config.get('commonInfo', 'address2'))
        return address2

    @staticmethod
    def zipcode():
        zipcode = (config.get('commonInfo', 'zipcode'))
        return zipcode

    @staticmethod
    def phonenum():
        phonenum = (config.get('commonInfo', 'phonenum'))
        return phonenum

    @staticmethod
    def faxnum():
        faxnum = (config.get('commonInfo', 'faxnum'))
        return faxnum

# Payment details for credit card


    @staticmethod
    def cardtype():
        cardtype = (config.get('commonInfo', 'cardtype'))
        return cardtype

    @staticmethod
    def cardholdername():
        cardholdername = (config.get('commonInfo', 'cardholdername'))
        return cardholdername

    @staticmethod
    def cardnumber():
        cardnumber = (config.get('commonInfo', 'cardnumber'))
        return cardnumber

    @staticmethod
    def expdate_month():
        expdate_month = (config.get('commonInfo', 'expdate_month'))
        return expdate_month

    @staticmethod
    def expdate_year():
        expdate_year = (config.get('commonInfo', 'expdate_year'))
        return expdate_year

    @staticmethod
    def cardcode():
        cardcode = (config.get('commonInfo', 'cardcode'))
        return cardcode

# password change

    @staticmethod
    def oldpwd():
        oldpwd = (config.get('commonInfo', 'oldpwd'))
        return oldpwd

    @staticmethod
    def newpwd():
        newpwd = (config.get('commonInfo', 'newpwd'))
        return newpwd

    @staticmethod
    def confirmpwd():
        confirmpwd = (config.get('commonInfo', 'confirmpwd'))
        return confirmpwd

#My Account > Downloadable products

    @staticmethod
    def first_dp():
        first_dp = (config.get('commonInfo', 'first_dp'))
        return first_dp

    @staticmethod
    def last_dp():
        last_dp = (config.get('commonInfo', 'last_dp'))
        return last_dp

    @staticmethod
    def email_dp():
        email_dp = (config.get('commonInfo', 'email_dp'))
        return email_dp

    @staticmethod
    def password_dp():
        password_dp = (config.get('commonInfo', 'password_dp'))
        return password_dp



# print(ReadConfig.getApplicationURL())
# print(ReadConfig.getUseremail())
# print(ReadConfig.searchItem())
# print(ReadConfig.wishlist_to_delete())
# print(len(ReadConfig.wishlist_to_add()))
