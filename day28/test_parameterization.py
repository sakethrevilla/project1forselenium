import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

class Testclass:
    @pytest.mark.parametrize('user,pwd',[("standard_user","secret_sauce"),("performance_glitch_user","secret_sauce"),("adm","admin123"),("Admin","adm"),])

    def test_login(self,user,pwd):
        self.object = Service("C:/driver/chromedriver-win32/chromedriver.exe")
        self.driver=webdriver.Chrome(service=self.object)

        self.driver.get("https://www.saucedemo.com/")
        self.driver.maximize_window()
        self.driver.find_element(By.NAME, value="user-name").send_keys("standard_user")
        self.driver.find_element(By.ID, value="password").send_keys("secret_sauce")
        self.driver.find_element(By.ID, value="login-button").click()

        try:
            self.status=self.driver.find_element(By.XPATH,"//div[@class='app_logo']").is_displayed()
            self.driver.close()
            assert self.status==True
        except:
            self.driver.close()
            assert False





