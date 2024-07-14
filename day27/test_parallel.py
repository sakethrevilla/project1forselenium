import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By

class Testlogin:
    def test_login_chrome(self):
        from selenium.webdriver.chrome.service import Service
        self.serv_obj = Service("C:\Drivers\chromedriver_win32\chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serv_obj)
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID,"user-name").send_keys("standard_user")
        self.driver.find_element(By.ID,"password").send_keys("secret_sauce")
        self.driver.find_element(By.ID,"login-button").click()
        assert self.driver.title=="Swag Labs"
        self.driver.quit()


    def test_login_edge(self):
        from selenium.webdriver.edge.service import Service
        self.serv_obj = Service("C:\driver\msedgedriver.exe")
        self.driver = webdriver.Edge(service=self.serv_obj)
        self.driver.get("https://www.saucedemo.com/")
        self.driver.find_element(By.ID, "user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, "password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, "login-button").click()
        assert self.driver.title == "Swag Labs"
        self.driver.quit()



