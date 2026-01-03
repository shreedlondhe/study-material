from selenium import webdriver
from selenium.webdriver.common.by import By
import logging

# Create and configure logger
logging.basicConfig(filename="CT8.log", format="%(asctime)s — %(name)s — %(levelname)s — %(funcName)s:%(lineno)d — %(message)s", filemode='a')
logger = logging.getLogger("Logger_Name")       # Create logger object with configuration and name

logger.setLevel(logging.DEBUG)      # Default logger level is logging.WARNING

try:

    logger.info('LoggingForFacebook.py script execution has been started...')
    logger.info('initializing web driver for chrome')
    driver = webdriver.Chrome()
    logger.info('initialized web driver for chrome')

    logger.debug('opening webpage or url : https://www.facebook.com/')
    driver.get("https://www.facebook.com/")
    logger.debug('opening webpage or url : https://www.facebook.com/')

    logger.info('Finding email element ')
    inputEmail = driver.find_element_by_id("emaidl")
    inputEmail.send_keys("sdfadf@gmail.com")

    inputPass = driver.find_element(By.ID, "pass")
    inputPass.send_keys("password@123")

    btnLogin = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')

    btnLogin.click()

    logger.info('test case passed')
except Exception as e:
    logger.error(f'Error occurred in facebook test : {e}')






