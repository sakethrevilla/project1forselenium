from selenium import webdriver

from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

object=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=object)


driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

window=driver.current_window_handle
print(window)
# # F136A3A104F2CD2F465567C9B31038F8 both the times window id are changing because they are generate dynamically on the browser they are not the part of webpage or web elements
# # C2A68EFDDA83365DB09CB97EDA694C49

# driver.find_element(By.XPATH,"/html/body/div/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a").click()