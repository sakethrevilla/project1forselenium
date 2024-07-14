
# handling alert for general applications like nakuari, instramgram where a element contains username and password

import requests
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

object=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=object)

driver.get("https://mail.rediff.com/cgi-bin/login.cgi")
driver.maximize_window()

# open alert
driver.find_element(By.XPATH,"//input[@title='Sign in']").click()
time.sleep(10)

# # handle the alerts
handlealert=driver.switch_to.alert
print(handlealert.text)
handlealert.dismiss()