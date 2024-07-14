import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://www.nakuari.com")
time.sleep(10)
driver.get("https://www.salesforce.com")
time.sleep(10)

driver.back()
driver.forward()

driver.refresh()

driver.quit()