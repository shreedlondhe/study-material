import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()

driver.get("https://seleniumbase.io/demo_page")

element = driver.find_element(By.ID, "mySelect")  # Find element on web page

dropdown = Select(element)  # create dropdown object with class Select # Select is accepting arguement to create dropdpwn object

# time.sleep(5)
# dropdown.select_by_index(2)  # select element/option by index
#
# time.sleep(5)
# dropdown.select_by_value("25%")  # select element/option by value attribute
#
# time.sleep(5)
# dropdown.select_by_visible_text("Set to 100%")  # select element/option by visible text on web page

all_option = dropdown.options           # get all option from select control or dropdown element
print(all_option)
for option in all_option:
    print(option.text)          #     print(option.get_attribute("innerHTML"))
    print(option.get_attribute('value'))



