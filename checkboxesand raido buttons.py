from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://www.lambdatest.com/selenium-playground/radiobutton-demo")
driver.maximize_window()
# selecting multiple
# l=driver.find_elements(By.XPATH,"//input[@name='prop']")
# print(len(l))
# approach1
# for x in range(len(l)):
#     l[x].click
# time.sleep(10)

# approach2

# for x in l:
#     x.click()
# selecting multiple checkboxes by choice

# selecting last 2 check boxes
# for x in range(len(l)-1,len(l)):
#     l[x].click()

#  selecting first 2 check boxes
# for x in range(len(l)):
#     if x<=1:
#         l[x].click()

# selecting only single checkbox
'''selecting multiple checkbox'''
checkbox=driver.find_elements(By.XPATH,"//input[@name='gender']")
print(len(checkbox))

# approach1
# for x in range(len(checkbox)):
#     checkbox[x].click()

# approach2
# for x in checkbox:
#     x.click()

# # 3 selecting the last two check boxes
# for x in range(len(checkbox)-1,len(checkbox)):
#     checkbox[x].click()
# selecting the first two checkboxes

# for x in range(len(checkbox)):
#     if x<=1:
#         checkbox[x].click()

#selecting the check boxes based on condition

for x in checkbox:
    tip=x.get_attribute("value")
    if tip=="male" or tip=='female':
        x.click()


