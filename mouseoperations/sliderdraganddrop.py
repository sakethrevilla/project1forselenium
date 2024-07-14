from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

slider=driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
print("the location of slider before moving")
print(slider.location)

act=ActionChains(driver)
act.drag_and_drop_by_offset(slider,200,0)
print(slider.location)