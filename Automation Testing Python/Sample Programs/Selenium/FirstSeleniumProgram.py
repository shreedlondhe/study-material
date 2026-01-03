from selenium import webdriver      # importing webdriver functionality from selenium module

#driver = webdriver.Chrome()     # creating chrome driver object
driver = webdriver.Chrome(executable_path="C:/Users/sss2327/AppData/Local/Programs/Python/Python39/chromedriver.exe")     # creating chrome driver object

driver.get("https://www.facebook.com/")         # open website/url

print("Page Title : ", driver.title)
print("Page Current Url : ", driver.current_url)

driver.back()       # back button on browser
driver.forward()       # forward button on browser

driver.close()      # close current window
driver.quit()       # Quits the driver and closes every associated window



###----------------------------------------------------------------------

### For latest version
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
#
# s=Service('C:/Users/Morteza/Documents/Dev/chromedriver.exe')
# browser = webdriver.Chrome(service=s)
# url='https://www.google.com'
# browser.get(url)