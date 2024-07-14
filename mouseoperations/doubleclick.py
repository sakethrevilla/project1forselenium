from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")
driver.maximize_window()
# doubleclick

driver.switch_to.frame("iframeResult")
frame1=driver.find_element(By.XPATH,"//input[@id='field1']")
frame1.clear()
frame1.send_keys("revilla")

frame2=driver.find_element(By.XPATH,"//input[@id='field2']")
act=ActionChains(driver)
act.double_click(frame2).perform()