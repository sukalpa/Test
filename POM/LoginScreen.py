from selenium import webdriver
from selenium.webdriver.common.by import By
class Login:

    Login_ID = "//input[@id='Email']"
    Password_ID = "//input[@id='Password']"
    Login_Button = "//button[contains(text(),'Log in')]"
    button_logout_xpath = "//a[contains(text(),'Logout')]"

    def __init__(self,driver):
        self.driver = driver

    def setusername(self,username):
        self.driver.find_element_by_xpath(self.Login_ID).clear()
        self.driver.find_element_by_xpath(self.Login_ID).send_keys(username)
    def setpassword(self,password):
        self.driver.find_element_by_xpath(self.Password_ID).clear()
        self.driver.find_element_by_xpath(self.Password_ID).send_keys(password)
    def cliklogin(self):
        self.driver.find_element_by_xpath(self.Login_Button).click()
    def logout(self):
        self.driver.find_element_by_xpath(self.button_logout_xpath).click()

