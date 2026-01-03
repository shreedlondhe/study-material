import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

driver.find_element(By.XPATH, '//*[@id="start"]/button').click()

eleH4 = WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located((By.XPATH, '//*[@id="finish"]/h4') ))

#eleH4 = driver.find_element(By.XPATH, '//*[@id="finish"]/h4')
print(eleH4.get_attribute("innerHTML"))
