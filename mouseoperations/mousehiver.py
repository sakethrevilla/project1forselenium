from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
