from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Loginpageobjects import LoginPage

class TestLogin:
    def test_login(self):
        serv_obj = Service("C:\\Drivers\\chromedriver_win32\\chromedriver.exe")
        self.driver=webdriver.Chrome(service=serv_obj)
        self.driver.get("https://admin-demo.nopcommerce.com/login")
        self.driver.maximize_window()

        self.lp=LoginPage(self.driver)
        self.lp.setUserName("admin@yourstore.com")
        self.lp.setPassword("admin")
        self.lp.clickLogin()
        self.act_title=self.driver.title
        self.driver.close()
        assert self.act_title == "Dashboard / nopCommerce administration"




