from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains, Keys
import time

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

input1=driver.find_element(By.XPATH,"//input[@id='name']")
input2=driver.find_element(By.XPATH,"//input[@id='email']")

input1.send_keys("revilla saketh naidu")

act=ActionChains(driver)

# selecting the text from inputA
#
# act.key_down(Keys.CONTROL)
# act.send_keys("a")
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
time.sleep(5)
# coping the selected input

# act.key_down(Keys.CONTROL)
# act.send_keys("c")
# act.key_up(Keys.CONTROL)
# act.perform()

act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
time.sleep(2)
# changing from one tab to another tab

act.send_keys(Keys.TAB)
act.perform()
time.sleep(5)
# now changing the data from one tab to another tab

act.key_down(Keys.CONTROL)
act.send_keys("V")
act.key_up(Keys.CONTROL)
act.perform()
time.sleep(5)
print(input2.text)