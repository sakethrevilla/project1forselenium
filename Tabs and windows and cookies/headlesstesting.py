from selenium import webdriver

def headless_chrome():
    from selenium.webdriver.chrome.service import Service
    obj = Service("C:/driver/chromedriver-win32/chromedriver.exe")
    ops=webdriver.ChromeOptions()
    ops.headless=True
    driver = webdriver.Chrome(service=obj,options=ops)
    return driver


driver=headless_chrome()
driver.get("https://nakuari.com/")
print(driver.title)
print(driver.current_url)

