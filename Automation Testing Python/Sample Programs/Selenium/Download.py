import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/download")
time.sleep(3)

driver.find_element(By.LINK_TEXT, 'batch 21.png').click()
