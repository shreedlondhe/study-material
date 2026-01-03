import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_alert")

driver.switch_to.frame('iframeResult')      # go and search element in perticular frame
elementJsButton = driver.find_element(By.XPATH, '/html/body/button')
time.sleep(4)
elementJsButton.click()
time.sleep(4)
driver.switch_to.alert.accept()         # click on Ok button from popup/alert
