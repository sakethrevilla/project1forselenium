from selenium import webdriver

from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By

object=Service("C:/driver/chromedriver-win32/chromedriver.exe")

driver=webdriver.Chrome(service=object)

driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

# driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[1]/div/div/div[2]/div/div/div/input")
# driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[1]/div/button/span[2]")

# driver.find_element(By.XPATH,"/html/body/div[3]/div[2]/div[1]/div/div/div[2]/div/div/div/input")


# driver.find_element(By.XPATH,"//input[@placeholder='Username']")

# or
# driver.find_element(By.XPATH,"//input[@ name='username' or class = 'oxd-input oxd-input--active' ]")

# contains() & starts-with()

# driver.find_element(By.XPATH,"//input[@ name='username' or class = 'oxd-input oxd-input--active' ]")

driver.find_element(By.XPATH,"//input[contains(@name,'username')]").send_keys("T")
