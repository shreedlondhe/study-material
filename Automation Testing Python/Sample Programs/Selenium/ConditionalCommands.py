from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://seleniumbase.io/demo_page")

dropElement = driver.find_element(By.ID, "drop1")
print("is drop element visible to user : ", dropElement.is_displayed())

# if(dropElement.is_displayed() == "False"):
checkElement = driver.find_element(By.ID, "checkBox1")
print("is checkbox is enable for click : ", checkElement.is_enabled())
checkElement.click()

print("After checkbox click, is drop element visible to user : ", dropElement.is_displayed())

if dropElement.is_displayed():         #if(dropElement.is_displayed() == True)
    print("Test case passed")
else:
    print("Test case failed")



