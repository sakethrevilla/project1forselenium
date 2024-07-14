 # implict wait
# from selenium import webdriver
#
# from selenium.webdriver.chrome.service import Service
#
# from selenium.webdriver.common.by import By
# import time
#
# obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
# driver=webdriver.Chrome(service=obj)
# driver.implicitly_wait(10)
#
# driver.get("https://www.naukri.com/nlogin/login")
# driver.maximize_window()
#
# try:
#     driver.find_element(By.XPATH,"//input[@id='usernameField']")
#     print("the element is found")
# except:
#     print("no such element is found")

#**************explict wait****************************

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

from selenium.webdriver.support.wait import WebDriverWait

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

mywait=WebDriverWait(driver,10)

driver.get("https://www.naukri.com/nlogin/login")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='usernameField']").send_keys("sakethrevilla0119@gmail.com")
driver.find_element(By.XPATH,"//input[@id='passwordField']").send_keys("Joy@19ce")
driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()

mywait.until(EC.presence_of_element_located(By.XPATH,"//div[contains(text(),'Applies (15)')]")).click()



