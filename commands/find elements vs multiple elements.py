import time
from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://demo.nopcommerce.com/login")

#############find_element()-  returns single element

# driver.find_element(By.XPATH,"//*[@id='small-searchterms']").send_keys("saketh revilla")
# time.sleep(12)

# locators matching with multiple elements

# k=driver.find_elements(By.XPATH,"// div[@class='footer-block information']//a")
# print(len(k))

# # if the elements are not avaliable then throws occur
# k=driver.find_element(By.LINK_TEXT,"saketh")
#****************************8find_elements()-  returns multiple elements
# locator matches with the single element
# elements=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(elements))


# locator matches with the multiple elements

# elements=driver.find_elements(By.XPATH,"//div[@class='footer']//a")
# for ele in elements:
#     print(ele.text)

# if the element is not available

elements=driver.find_elements(By.LINK_TEXT,"saketh")
print(len(elements))

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@difference betwwen text and get_attribute

# email=driver.find_element(By.XPATH,"//input[@id='Email']")
# email.clear()
# email.send_keys("sakethrevilla0119@gmail.com")

# print("the text value of the box is:",email.text)
# print("the value of the box is",email.get_attribute('value'))

button=driver.find_element(By.XPATH,"//button[normalize-space()='Log in']")
print("result is:",button.text)
print("the result is:",button.get_attribute('value'))