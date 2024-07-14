from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj=Service("C:\driver\chromedriver-win32\chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.get("https://www.saucedemo.com/")
driver.find_element(By.NAME, value="user-name").send_keys("standard_user")
driver.find_element(By.ID, value="password").send_keys("secret_sauce")
driver.find_element(By.ID, value="login-button").click()

Act_logo=driver.title
Exp_logo="Swag Labs"

if Act_logo == Exp_logo:
    print("logo test passed")
else:
    print("logo test not passed")
driver.close()



















# from selenium import webdriver
#
# from selenium.webdriver.chrome.service import service
#
# from selenium.webdriver.common.by import By
#
# obj=service("C:\driver\chromedriver-win32\chromedriver.exe")
# driver=webdriver.Chrome(service=obj)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj=Service("C:\driver\chromedriver-win32\chromedriver.exe")
driver=webdriver.Chrome(service=obj)