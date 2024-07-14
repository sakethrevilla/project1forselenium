from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
import os
import time

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

# driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
# driver.maximize_window()
# time.sleep(5)
#
#   # here we are opening a website and we are transferring from one to another by clicking that link
newtab=Keys.CONTROL+Keys.RETURN
# driver.find_element(By.XPATH,"//a[contains(text(),'Buy Ticket')]").send_keys(newtab)
# time.sleep(5)

# here we are opening the two different websites in two different tabs

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

driver.switch_to.new_window('tab')

driver.get("https://www.nakuari.com/")