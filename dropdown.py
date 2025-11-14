from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dropdown")
dropdown_element= driver.find_element(By.ID,"dropdown")
dropdown_element.click()
dropdown= Select(dropdown_element)
time.sleep(2)
dropdown.select_by_visible_text("Option 1")
time.sleep(2)
selected_option=dropdown.first_selected_option.text
time.sleep(2)
assert selected_option=="Option 1",f"Selected option is 'Option 1', but {selected_option}"
print("Test Passed")
print(selected_option)
driver.quit()


