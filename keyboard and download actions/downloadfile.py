from selenium import webdriver
from selenium.webdriver.common.by import By

def chrome_setup():
    from selenium.webdriver.chrome.service import Service
    obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
    preferences={"download.default_directory":"D:/project1forselenium/keyboard and download actions"}
    driver=webdriver.Chrome(service=obj)
    return driver
driver=chrome_setup()

driver.get("https://file-examples.com/index.php/sample-documents-download/sample-doc-download/")
driver.maximize_window()

driver.find_element(By.XPATH,"//tbody/tr[1]/td[5]/a[1]").click()
