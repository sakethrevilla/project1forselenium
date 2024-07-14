import requests
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

object=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=object)

driver.get("http://demo.automationtesting.in/Frames.html")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[normalize-space()='Iframe with in an Iframe']").click()

outerframe=driver.find_element(By.XPATH,"//iframe[@src='MultipleFrames.html']")
driver.switch_to.frame(outerframe)

innerframe=driver.find_element(By.XPATH,"/html/body/section/div/div/iframe")
driver.switch_to.frame(innerframe)

driver.find_element(By.XPATH,"/html/body/section/div/div/div/input").send_keys("revill")

time.sleep(10)
driver.switch_to.parent_frame()