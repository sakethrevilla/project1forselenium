from selenium import webdriver

from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.common.by import By

object=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=object)

driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407")
driver.maximize_window()

#selecting a single checkbox from a page
driver.find_elements(By.XPATH,"//label[text()='What days of the week are you consistently available?']/following-sibling::div//input[@type='checkbox']")


time.sleep(20)

# //label[@for='RESULT_CheckBox-8_3']
#
# // input[ @ id = 'RESULT_CheckBox-8_3']






