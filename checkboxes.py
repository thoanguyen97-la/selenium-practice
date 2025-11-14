from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/checkboxes")
time.sleep(2)
checkboxes= driver.find_elements(By.CSS_SELECTOR,"input[type='checkbox']")
print(f"Before click:checkbox 1 {checkboxes[0].is_selected()}, checkbox2 {checkboxes[1].is_selected()}")
checkboxes[0].click()
time.sleep(2)
print(f"After click:checkbox 1 {checkboxes[0].is_selected()}, checkbox2 {checkboxes[1].is_selected()}")
#untick checkbox
for checkbox in checkboxes:
    if checkbox.is_selected():
        checkbox.click()
        time.sleep(2)
assert checkboxes[0].is_selected()==False
assert checkboxes[1].is_selected()==False
driver.quit()
