import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By


ops=webdriver.ChromeOptions()
ops.add_argument("--disable-notifications")

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https:\\whatmylocation.com/")
driver.maximize_window()