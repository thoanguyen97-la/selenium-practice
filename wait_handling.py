from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
wait = WebDriverWait(driver, 10)

driver.find_element(By.XPATH,"//button[text()='Start']").click()

hello = wait.until(EC.visibility_of_element_located((By.XPATH,"//h4[text()='Hello World!']"))).text
assert hello == "Hello World!"
print("✅ Hello world! appear - Test passed!")
driver.quit()
