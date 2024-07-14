import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2Fregister")
driver.maximize_window()
# x= driver.title
#
# exp_output = "orangeHRm"
#
# if x==exp_output:
#     print("test case passed")
# else:
#     print("test case not passed")
# print(driver.current_url)
# print(driver.page_source)

#************************ conditional commands ***************************

# is displayed is enabled
# searchbox=driver.find_element(By.XPATH,"//*[@id='small-searchterms']")
# print("display status is:",searchbox.is_displayed())
# print("Enabled status is:",searchbox.is_enabled())

#is_selected or not these are used for raido buttons and search boxes only
male=driver.find_element(By.XPATH,"//*[@id='gender-male']")
print(male.is_selected())

time.sleep(60)