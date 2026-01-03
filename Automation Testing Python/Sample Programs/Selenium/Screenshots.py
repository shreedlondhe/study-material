from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()

driver.get("https://www.facebook.com/")

driver.get_screenshot_as_file("C:/Development/Class/Python/CT8/screenshotFacebook.png")

driver.save_screenshot('screenshotFacebook.png')
