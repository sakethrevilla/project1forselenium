from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://www.google.com/")
driver.implicitly_wait(15)
driver.maximize_window()

wait=driver.find_element(By.NAME,"q")
wait.send_keys("selenium")
wait.submit()

l=driver.find_elements(By.XPATH,"//h3[@ text='selenium']").click()
