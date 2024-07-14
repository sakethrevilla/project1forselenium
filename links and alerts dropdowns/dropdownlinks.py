from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

country=Select(driver.find_element(By.XPATH,"//select[@id='country']"))
# country.select_by_visible_text("France")
# country.select_by_value("10")
country.select_by_index(2)