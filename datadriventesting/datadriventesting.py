import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select

from day24 import XLUtils
obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)
driver.implicitly_wait(10)

driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india-sbi/fixed-deposit-calculator-SBI-BSB001.html")
driver.maximize_window()

file="F:/fdcalc.xlsx"
rows=XLUtils.getRowCount()
print(len(rows))
# reading the value from the table
for r in range(2,len(rows)+1):
    pric=XLUtils.readData(file,"Sheet1",r,1)
    rateintesert=XLUtils.readData(file,"Sheet1",r,2)
    per1=XLUtils.readData(file,"Sheet1",r,3)
    per2=XLUtils.readData(file,"sheet1",r,4)
    fre=XLUtils.readData(file,"sheet1",r,5)
    expvalue=XLUtils.readData(file,"sheet1",r,6)
# passing the data for the fields

    driver.find_element(By.XPATH,"//input[@id='principal']").send_keys(pric)
    driver.find_element(By.XPATH,"//input[@id='interest']").send_keys(rateintesert)
    driver.find_element(By.XPATH,"//input[@id='tenure']").send_keys(per1)
    tim=Select(driver.find_element(By.XPATH,"//select[@id='tenurePeriod']"))
    tim.select_by_visible_text(per2)

    frequency=Select(driver.find_element(By.XPATH,"//select[@id='frequency']"))
    frequency.select_by_visible_text(fre)

    driver.find_element(By.XPATH,"//img[@src='https://images.moneycontrol.com/images/mf_revamp/btn_calcutate.gif']").click()
    actualvalue=driver.find_element(By.XPATH,"//span[@id='resp_matval']/strong").text

    # valadition

    if float(expvalue)==float(actualvalue):
        print("testcase success")
        XLUtils.writeData(file,"Sheet1",r,8,"passed")
        XLUtils.fillRedColor(file,"Sheet1",r,8)

    else:
        print("testfailed")
        XLUtils.writeData(file,"Sheet1",r,8,"failed")
        XLUtils.fillRedColor(file,"sheet1",r,8)