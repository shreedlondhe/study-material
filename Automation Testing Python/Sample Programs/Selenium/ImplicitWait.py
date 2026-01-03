import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

driver.find_element(By.XPATH, '//*[@id="start"]/button').click()

###time.sleep(10)       #  python - script will stop execution for 10 sec

#it will be applicable for all controls
driver.implicitly_wait(120)     # selenium- it will pause/wait for maximun 120 to appear element on page and minimum 0 sec
eleH4 = driver.find_element(By.XPATH, '//*[@id="finish"]/h4')
print(eleH4.get_attribute("innerHTML"))
