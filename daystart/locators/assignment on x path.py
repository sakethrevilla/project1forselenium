from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

# ancestor nodes

# msg=driver.find_element(By.XPATH,"//a[contains(text(),'Bajaj HindusthanSuga')]/ancestor::tr").text
# print(msg)

#desendent

# msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Bajaj HindusthanSuga')]/ancestor::tr/descendant::*")
# print(len(msg))

# following
msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Bajaj HindusthanSuga')]/ancestor::tr/following::td")
time.sleep(10)
print(len(msg))

# following-sibling
# msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Bajaj HindusthanSuga')]/ancestor::tr/following-sibling::*")
# time.sleep(10)
# print(len(msg))
