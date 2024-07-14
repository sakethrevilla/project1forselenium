from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

mywait=WebDriverWait(driver,10)

driver.get("https://www.google.com/")
driver.maximize_window()

exp=driver.find_element(By.NAME,"q")
exp.send_keys("selenium")
exp.submit()

search=mywait.until(EC.presence_of_element_located(By.XPATH,"//a[normalize-space()='Downloads']"
                                                            ""))
search.click()
