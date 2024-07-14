from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

# driver.get("https://www.naukri.com/")
driver.get("https://demo.nopcommerce.com/")
#
# # print(driver.title)
# # print(driver.current_url)
# # print(driver.page_source)
#
# comd=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# print("displaystatus is:",comd.is_displayed())
# print("selectedstatus is:",comd.is_enabled())

#********************difference between find_element()  or find_elements()

#find_element()

# locator matches with the single element

# element=driver.find_element(By.XPATH,"//input[@id='small-searchterms']").send_keys("nokia")
# print(element)

# locator matches with the multiple elements
# element=driver.find_element(By.XPATH,"//div[@class='footer-block information']//a")
# print(element.text)

# locator not matches with the multiple elements then we get exception
# element=driver.find_element(By.LINK_TEXT,"log")

#***********locator matches with the multiple elments we are also using the find_elements()
# locator matches with the single element
# elements=driver.find_elements(By.XPATH,"//input[@id='small-searchterms']")
# print(len(elements))


# locator matches with the multiple elements and we are also using the for loop to print the  test

# elements=driver.find_elements(By.XPATH,"//div[@class='footer-block information']//a")
# print(len(elements))
#
# for x in elements:
#     print(x.text)

# if the elements are not avaliable then we are not get the excepation

elements=driver.find_elements(By.ID,"12")
print(len(elements))
