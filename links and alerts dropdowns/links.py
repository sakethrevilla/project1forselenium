import requests
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

object=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=object)
# 8888888888888888********normal links practice
# driver.get("https://demo.nopcommerce.com")
# driver.maximize_window()
#
# links=driver.find_elements(By.XPATH,"//a")
# print(len(links))
#
# for x in links:
#     print(x.text)

# broken links practice

driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()

# links=driver.find_elements(By.TAG_NAME,'a')
# count=0
#
# for link in links:
#     url=link.get_attribute("href")
#     res=requests.head(url)
#
#     if res.status_code>=400:
#         print(url,"is broken")
#         count=count+1
#     else:
#         print(url,"link is not broken")

# link=driver.find_elements(By.TAG_NAME,'a')
# /print(len(link))
#
# for x in link:
#     print(x.text)

links=driver.find_elements(By.TAG_NAME,'a')
count=0
for link in links:
    url=link.get_attribute("href")
    res=requests.head(url)
    if res.status_code>=400:
        print(url,)
    else:
        print(url)