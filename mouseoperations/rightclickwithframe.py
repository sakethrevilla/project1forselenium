from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
import time

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()


button=driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
act=ActionChains(driver)
act.context_click(button).perform()

driver.find_element(By.XPATH,"/html/body/ul/li[1]/span").click()

driver.switch_to.alert.accept()
