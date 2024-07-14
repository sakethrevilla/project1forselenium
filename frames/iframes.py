# import requests
# from selenium import webdriver
#
# from selenium.webdriver.chrome.service import Service
# import time
# from selenium.webdriver.common.by import By
#
# object=Service("C:/driver/chromedriver-win32/chromedriver.exe")
# driver=webdriver.Chrome(service=object)
#
# driver.get("https://example.com/")
# driver.maximize_window()
#
# driver.find_element(By.XPATH,"//a[normalize-space()='More information...']").click()
#
# # now we are entring to frames concept
#
# frame1=driver.find_element(By.XPATH,"//a[normalize-space()='Domains']").click()
# # driver.switch_to.frame(frame1)
#
# driver.find_element(By.XPATH,"//a[normalize-space()='Root Zone Management']").click()
#
# # driver.switch_to.default_content()
#
# # now we are going to secong frames
#
# frame2=driver.find_element(By.XPATH,"//div[@class='navigation']//a[normalize-space()='Protocols']").click()
# # driver.switch_to.frame(frame2)
#
# driver.find_element(By.XPATH,"//li[@id='nav_prot_tz']").click()
# # driver.switch_to.default_content()

import requests
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

object=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=object)

driver.get("https://www.geeksforgeeks.org/python-programming-language-tutorial/")
driver.maximize_window()

