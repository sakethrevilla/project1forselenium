from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os
import time

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")

# finding the length of the cookies
# cookie=driver.get_cookies()
# print(len(cookie))

# capture the cookies from the browse
# cookie=driver.get_cookies()
# print(len(cookie))
# for cook in cookie:
#     # print(cook.get('name'))
#     # print(cook.get('value'))

# adding the new cookie to the browsers

# driver.add_cookie({"name":"saketh","value":"123"})
# cookies=driver.get_cookies()
# print(len(cookies))
# for x in cookies:
#     print(x.get('name'))

# deleting the specific cookies from the browsers

# driver.delete_cookie("saketh")
# cookies=driver.get_cookies()
#
# for x in cookies:
#     print(x.get('name'))
#

driver.delete_all_cookies()
x=driver.get_cookies()
print(len(x))