from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")

wait = WebDriverWait(driver, 10)

#1 Thao tác với JS Alert
driver.find_element(By.XPATH,"//button[text()='Click for JS Alert']").click()
js_alert= wait.until(EC.alert_is_present())
js_alert.accept()
msg= driver.find_element(By.ID,"result").text
assert "You successfully clicked an alert" in msg
print("✅ JS Alert passed!")

#2 Thao tác với JS Confirm: OK
driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
js_confirm= wait.until(EC.alert_is_present())
js_confirm.accept()
msg= driver.find_element(By.ID,"result").text
assert "You clicked: Ok" in msg
print("✅ JS Confirm(OK) passed!")

#2 Thao tác với JS Confirm: Cancel
driver.find_element(By.XPATH,"//button[text()='Click for JS Confirm']").click()
js_confirm= wait.until(EC.alert_is_present())
js_confirm.dismiss()
msg= driver.find_element(By.ID,"result").text
assert "You clicked: Cancel" in msg
print("✅ JS Confirm(Cancel) passed!")

#Thao tác với JS Prompt: input text and click OK
driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
js_prompt= wait.until(EC.alert_is_present())
js_prompt.send_keys("Hello Selenium")
js_prompt.accept()
msg= driver.find_element(By.ID,"result").text
assert "Hello Selenium" in msg
print("✅ JS Prompt(OK) passed!")

#Thao tác với JS Prompt: input text and click Cancel
driver.find_element(By.XPATH,"//button[text()='Click for JS Prompt']").click()
js_prompt= wait.until(EC.alert_is_present())
js_prompt.dismiss()
msg= driver.find_element(By.ID,"result").text
assert "null" in msg
print("✅ JS Prompt(Cancel) passed!")

driver.quit()
