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
# driver.get("https://the-internet.herokuapp.com/javascript_alerts")
# driver.maximize_window()
#
# # # open hanlde  alert for js alertwindow
# #
# # driver.find_element(By.XPATH,"//button[@onclick='jsAlert()']").click()
# # time.sleep(5)
# #
# # # handle alert
# #
# # handlealert=driver.switch_to.alert
# # print(handlealert.text)
# # time.sleep(10)
# # handlealert.dismiss()
#
# # handle alert for js prompt
#
# driver.find_element(By.XPATH,"//button[@onclick='jsPrompt()']").click()
# time.sleep(10)
#
# # now we are handling the alerts if we want to accept the alert the use accept() if no then use dismiss
# handlealert=driver.switch_to.alert
# print(handlealert.text)
#
# handlealert.send_keys("hi revilla saketh naidu")
# handlealert.dismiss()
# time.sleep(10)


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
# time.sleep(10)

driver.find_element(By.XPATH,"//a[normalize-space()='OrangeHRM, Inc']").click()

windowsids=driver.window_handles

parentid=windowsids[0]
childid=windowsids[1]

print(parentid)
print(childid)

driver.switch_to.window(parentid)
print("the title of the page is",driver.title)

driver.switch_to.window(childid)
print("the title of the page is",childid)
