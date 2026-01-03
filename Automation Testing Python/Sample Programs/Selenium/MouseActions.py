import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()

driver.get("https://seleniumbase.io/demo_page")
time.sleep(3)

action = ActionChains(driver)
eleDropdownHover = driver.find_element(By.ID, 'myDropdown')
eleOption3 = driver.find_element(By.ID, 'dropOption3')
action.move_to_element(eleDropdownHover).move_to_element(eleOption3).click().perform()


# Double click
#action.double_click(driver.find_element(By.ID, 'myButton')).perform()
eleButton = driver.find_element(By.ID, 'myButton')
action.double_click(eleButton).perform()

# right click
action.context_click().perform()











