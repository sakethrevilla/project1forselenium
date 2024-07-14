import requests
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

object=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=object)

driver.get("http://admin:admin@the-internet.herokuapp.com/basic_auth")
driver.maximize_window()
time.sleep(10)

# for some applications the pop will come before login to the website only it is not possible to handle those alerts also because there having to fields in that case we can bypass them by using

# this format https://username:password@link