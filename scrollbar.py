from selenium.common import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("http://www.uitestingplayground.com/scrollbars")
wait = WebDriverWait(driver,10)
#tìm button trong DOM
hidden_button = wait.until(EC.presence_of_element_located((By.ID,"hidingButton")))
# Scroll tới vị trí button 'center'
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hidden_button)
# chờ button clickable
hidden_button = wait.until(EC.element_to_be_clickable((By.ID,"hidingButton")))
hidden_button.click()
print("click thành công hidding button!")
driver.quit()




