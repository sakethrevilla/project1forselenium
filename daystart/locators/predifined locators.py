# from selenium import webdriver
#
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.by import By

# obj=Service("C:\driver\chromedriver-win32\chromedriver.exe")

# driver=webdriver.Chrome(service=obj)

# driver.get("https://www.naukri.com/nlogin/login")

# driver.find_element(By.ID,"usernameField").send_keys("sakethrevilla0119@gmail.com")
# driver.find_element(By.ID,"passwordField").send_keys("Joy@19ce")
# driver.find_element(By.LINK_TEXT, value="Login").click()
# links=driver.find_element(By.TAG_NAME,'a')
# print(len(links))

"""from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")

driver=webdriver.Chrome(service=obj)


driver.get("https://www.facebook.com/")
driver.maximize_window()

tag and id
driver.find_element(By.CSS_SELECTOR,"input#email" )

tag and class
driver.find_element(By.CSS_SELECTOR,"input.inputtext").send_keys("sakethrevilla191@gmail.com")

tag and attribute

driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal_email]").send_keys("revilla saketh")

tagclassname and attribute

driver.find_element(By.CSS_SELECTOR,"input.inputtext[data-testid=royal_email]").send_keys("sakethrevilla0119@gmail.com")"""



# instagram for css selector

from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")

driver=webdriver.Chrome(service=obj)

driver.get("https://www.naukri.com/nlogin/login")
#
# # tag name &id
# # driver.find_element(By.CSS_SELECTOR,"input#usernameField").send_keys("revilla saketh naidu")
#
# #tag class
#
# driver.find_element(By.CSS_SELECTOR,"")

