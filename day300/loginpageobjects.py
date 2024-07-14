from selenium import webdriver
from selenium.webdriver.common.by import By


class Loginpage:
    # locators

    link_login_id = "login_Layer"
    txt_username_xpath = "//input[@placeholder='Enter your active Email ID / Username']"
    txt_password_xpath = "//input[@placeholder='Enter your password']"
    button_login_xpath = "//button[@type='submit']"

    # constructors
    def __init__(self, driver):
        self.driver = driver

    # action methods
    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.link_login_id).click()

    def setuserName(self, username):
        usernametxt = self.driver.find_element(By.XPATH, self.txt_username_xpath)
        usernametxt.clear()
        username.send_keys(username)

    def setpassword(self, pwd):
        passwordtxt = self.driver.find_element(By.XPATH, self.txt_password_xpath)
        passwordtxt.clear()
        passwordtxt.send_keys(pwd)

    def Login(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()