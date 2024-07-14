from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys("selenium")
driver.find_element(By.XPATH,"//input[@type='submit']").click()
time.sleep(10)

driver.find_element(By.XPATH,"//a[normalize-space()='Selenium']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Selenium in biology']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Selenium (software)']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Selenium disulfide']").click()
driver.find_element(By.XPATH,"//a[normalize-space()='Selenium dioxide']").click()

windowsIDs=driver.window_handles

#
# parentwindowid=windowsIDs[0]
# childwindowid=windowsIDs[1]
#
# print(parentwindowid,childwindowid)
# approach-1 this is stuabile if we have only 2 or 3 windows if we have more windows then we need to use the fro loop because by using typing it would be the difficult to access.

# driver.switch_to.window(parentwindowid)
# print("the titile of parent browser is:",driver.title)
#
# driver.switch_to.window(childwindowid)
# print("the title of child windowis:",driver.title)

# appoach2

# for x in windowsIDs:
#     driver.switch_to.window(x)
#
#     if driver.title=="Selenium dioxide - Wikipedia" or "Selenium (software) - Wikipedia":
#         print(driver.title)
#         driver.close()



