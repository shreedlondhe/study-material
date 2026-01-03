from selenium import webdriver      # importing webdriver functionality from selenium module
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()     # creating chrome driver object
driver.get("https://seleniumbase.io/demo_page")         # open website/url

inputElement = driver.find_element(By.ID, "myTextInput2")
inputText = inputElement.get_attribute("value")  # Read value/text from value attribute
print("Input Text : ", inputText)

inputElement.clear()
inputElement.send_keys("new text")

print("Input Text : ", driver.find_element(By.ID, "myTextInput2").get_attribute("value"))

print("Input field name : ", driver.find_element(By.ID, "myTextInput2").get_attribute("name"))