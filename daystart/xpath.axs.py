from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://money.rediff.com/gainers/bse/daily/groupa")
driver.maximize_window()
#self
# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Avanti Feeds')]/self::a").text

# driver.find_element(By.XPATH,"/html/body/div[2]/div[5]/table/tbody/tr[1]/td[1]/a")
#parent
# driver.find_element(By.XPATH,"//a[contains(text(),'Avanti Feeds')/parent::td").text


# text_msg=driver.find_element(By.XPATH,"//a[contains(text(),'Avanti Feeds')/parent::td").text
# print(text_msg)

# child

# childs=driver.find_elements(By.XPATH,"//a[contains(text(),'Avanti Feeds')/ancestor::tr/child::td")
# print(len(childs)

# ancestor

# text_msg = driver.find_elements(By.XPATH, "//a[contains(text(),'Avanti Feeds')/ancestor::tr").txt
# print(text_msg)

# decendant

# descendants = driver.find_elements(By.XPATH, "//a[contains(text(),'Avanti Feeds')/ancestor::tr/descendant::*")
# print("numbers of descendant nodes : ",len(descendants))

#  following




