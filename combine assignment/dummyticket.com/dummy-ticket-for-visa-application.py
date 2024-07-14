from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
# # clicking checkbox
# driver.find_element(By.XPATH,"//input[@id='product_549']").click()
# time.sleep(1)

# Passenger details:

# driver.find_element(By.XPATH,"//input[@id='travname']").send_keys("saketh")
# driver.find_element(By.ID,"travlastname").send_keys("revilla")
# driver.find_element(By.ID,"dob").send_keys("19/01/2002")
# # driver.find_element(By.XPATH,"//input[@id='sex_1']").click()
# time.sleep(5)
# # Travel Details
# # driver.find_element(By.ID,"traveltype").click()
# driver.find_element(By.XPATH,"//input[@id='fromcity']").send_keys("tirupati")
# driver.find_element(By.XPATH,"//input[@id='tocity']").send_keys("hyderabad")
# time.sleep(5)
# # date
# driver.find_element(By.XPATH,"//input[@id='departon']").click()
# mon=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
# mon.select_by_visible_text("Jun")
# yr=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
# yr.select_by_visible_text("2024")
#
# # dates
# dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
#
# for date in dates:
#     if date.text==date:
#         date.click()
#         break

# # /delevary option
# dev=Select(driver.find_element(By.XPATH,"/html/body/span[2]/span/span[1]/input"))
# dev.select_by_visible_text("Other")


# billing country details
# con=Select(driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']"))
# # con.select_by_visible_text("Ind.ia")

# country

# conntry=driver.find_element(By.XPATH,"//input[@class='select2-search__field']")
# conntry.send_keys("India")
# conntry.click()
# time.sleep(20)


# bootstrap drop and down

driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()

countries=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
print(len(countries))

for country in countries:
    if country.text=="India":
        country.click()
        break
time.sleep(10)