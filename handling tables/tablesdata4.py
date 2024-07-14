#counting the no.of rows and colomuns in a table
# counting the specific row and colonum data based on xpath
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
# counting no.of rows and colomuns in a table

rows=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
colomuns=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th")
# # print(len(rows))
# # print(len(colomuns))
# print()

# read the specific row and colonum data price 3000

row1=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[1]//th[4]")
row2=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[7]//td[2]")
print(row1.text)
print(row2.text)

# print()

# read all the rows and colonum data in a table manner there we can use the end='' to print the data in side by side
# print("printing all the rows and colonums data....................")
#
# rows=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr")
# colomuns=driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th")
#
# for r in range(2,len(rows)+1):
#     for c in range(1,len(colomuns)+1):
#         data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+ str(r)+"]/td["+str(c)+"]").text
#         print(data,end='')
#     print()

# selecting the rows based on the conditions
#
# for i in range(2,len(rows)+1):
#
#     authorname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(i)+"]/td[2]").text
#
#     if authorname=='Animesh':
#         bookname=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(i)+"]/td[1]").text
#         price=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(i)+"]/td[4]").text
#
#         print(bookname,"  ",price)
#


