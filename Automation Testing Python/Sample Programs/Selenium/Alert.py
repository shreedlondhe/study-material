import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/javascript_alerts")

elementJsButton = driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[2]/button')
time.sleep(4)
elementJsButton.click()
time.sleep(4)
driver.switch_to.alert.accept()         # click on Ok button from popup/alert

#driver.switch_to.alert.dismiss()        # click on cancel button from popup/alert














