from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

parent=driver.find_element(By.ID,"box2")
child=driver.find_element(By.ID,"box106")
act=ActionChains(driver)
act.drag_and_drop(parent,child)
time.sleep(10)