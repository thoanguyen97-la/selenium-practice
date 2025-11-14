from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver= webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/login")
time.sleep(5)
driver.find_element(By.ID, "username").send_keys("tomsmith")
driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(3)
msg= driver.find_element(By.ID,"flash").text
assert "You logged into a secure area!" in msg

