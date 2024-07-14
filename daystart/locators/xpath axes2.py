from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()

# self tag
# msg=driver.find_element(By.XPATH,"//a[contains(text(),'Dilip Buildcon Ltd.')]/self::a").text
# print(msg)

# # parent tag
# msg=driver.find_element(By.XPATH,"//a[contains(text(),'Dilip Buildcon Ltd.')]/parent::td").text
# print(msg)

# childs tags
# msg=driver.find_elements(By.XPATH,"//a[contains(text(),'Dilip Buildcon Ltd.')]/ancestor::tr/child::td")
# print(len(msg))
# for x in msg:
#     print(x.text,end="")

# ancestor nodes

msg=driver.find_element(By.XPATH,"//a[contains(text(),'Dilip Buildcon Ltd.')]/ancestor::tr").text
print(msg)

# decendant

# descendants=driver.find_elements(By.XPATH,"//a[contains(text(),'Dilip Buildcon Ltd.')]/ancestor::tr/descendant::*")
# print(len(descendants))
#
# # following
# following=driver.find_elements(By.XPATH,"//a[contains(text(),'Dilip Buildcon Ltd.')]/ancestor::tr/following::*")
# print(len(following))
