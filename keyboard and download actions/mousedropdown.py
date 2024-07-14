from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()

#selecting the countries name

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()

countries=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(countries))

# printing countries names

for country in countries:
# print(country.text)
    if country.text=='India':
        country.click()
        break
time.sleep(10)