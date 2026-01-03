from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/")

inputEmail = driver.find_element_by_id("email")
inputEmail.send_keys("sdfadf@gmail.com")

inputPass = driver.find_element(By.ID, "pass")
inputPass.send_keys("password@123")

#btnLogin = driver.find_element(By.NAME, "login")
#btnLogin = driver.find_element(By.XPATH, '//*[@id="u_0_d_mP"]')     # copy Xpath # it will not work in facebook.com for logging btn
#btnLogin = driver.find_element(By.XPATH, '//*[@name="login"]')     # copy Xpath # it will not work in facebook.com for logging btn
btnLogin = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')

btnLogin.click()






