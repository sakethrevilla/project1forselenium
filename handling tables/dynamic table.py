from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

obj=Service("C:/driver/chromedriver-win32/chromedriver.exe")
driver=webdriver.Chrome(service=obj)

driver.get("https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)")
driver.maximize_window()

driver.find_element(By.XPATH,"//a[@href='#Table']//div[@class='vector-toc-text']").click()

# now we are handling the table data
# calculating the number of rows and colomuns in a table
# if we want to find the no.of rows in a colomun then we need to use{/tr}
# if we wnat to find the no.of colomuns in a table then we need to use{/tr[1]/th}
rows=driver.find_elements(By.XPATH,"//table[@class='wikitable sortable sticky-header-multi static-row-numbers jquery-tablesorter']//tr")
colonums=driver.find_elements(By.XPATH,"//table[@class='wikitable sortable sticky-header-multi static-row-numbers jquery-tablesorter']//tr[1]/th")
# print(len(rows))
# print(len(colonums))




# read the specific data
# con1=driver.find_element(By.XPATH,"//table[@class='wikitable sortable sticky-header-multi static-row-numbers jquery-tablesorter']//tr[40]/td[1]").text
# print(con1)

# read all the rows and colonums in table

# for r in range(2,len(rows)+1):
#     for c in range(1,len(colonums)+1):
#         data=driver.find_element(By.XPATH,"//table[@class='wikitable sortable sticky-header-multi static-row-numbers jquery-tablesorter']//tr["+str(r)+"]/td["+str(c)+"]").text
#         print(data,end="    ")
#     print()
#

# printing the data based on condition
count=0
for r in range(2,len(rows)+1):
    enthencity=driver.find_element(By.XPATH,"//table[@class='wikitable sortable sticky-header-multi static-row-numbers jquery-tablesorter']//tr["+str(r)+"]/td[2]").text
    if enthencity=="Americas":
        count=count+1
        foeecast=driver.find_element(By.XPATH,"//table[@class='wikitable sortable sticky-header-multi static-row-numbers jquery-tablesorter']//tr["+str(r)+"]/td[3]").text
        print(enthencity,"   ",foeecast)

    print()

print(count)