from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from loginpageobjects import Loginpage

class TestLogin:
    def test_login(self):
        serv_obj = Service("C://Drivers//chromedriver_win32//chromedriver.exe")
        self.driver=webdriver.Chrome(service=serv_obj)
        self.driver.get("https://www.naukri.com/")
        self.driver.maximize_window()

        self.lp=Loginpage(self.driver)
        self.lp.setuserName("sakethrevilla0119@gmail.com")
        self.lp.setpassword("Joy@19ce")
        self.lp.clickLogin()
        self.driver.close()

