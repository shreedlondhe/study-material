import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("https://the-internet.herokuapp.com/windows")

driver.find_element(By.XPATH, '//*[@id="content"]/div/a').click()

print("Cureently active window handle/id: ", driver.current_window_handle)  # handle/id current window

handles = driver.window_handles
print("All windows handle : ", handles)      #get all handle window open by script

driver.switch_to.window(handles[1])

textElement = driver.find_element(By.XPATH, '/html/body/div/h3')
print(textElement.text)


for handle in handles:
    driver.switch_to.window(handle)
    if driver.title == "Dashboard":
        break

# Do all the activities you wish to...


