from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://www.dummyticket.com/dummy-ticket-for-visa-application/")
driver.maximize_window()
# mon=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
# mon.select_by_visible_text("Jun")
#
# year=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select year']"))
# year.select_by_visible_text("2024")
#
# dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
#
# for date in dates:
#     if date.text=="29":
#         date.click()
#         break

driver.find_element(By.XPATH,"//input[@id='dob']").click()
mon=Select(driver.find_element(By.XPATH,"//select[@aria-label='Select month']"))
mon.select_by_visible_text("Jun")

time.sleep(5)

