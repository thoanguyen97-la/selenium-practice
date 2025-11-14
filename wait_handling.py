from selenium.common import TimeoutException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#🟩 1) EC.element_to_be_clickable
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/add_remove_elements/")
wait = WebDriverWait(driver, 10)
#chờ button add element clickable & click button
add_element = wait.until(EC.element_to_be_clickable((By.XPATH,"//button[text()='Add Element']")))
add_element.click()
#check hiển thị delete button
delete_element = wait.until(EC.visibility_of_element_located((By.XPATH,"//button[text()='Delete']")))
assert delete_element.text == "Delete"
print("1.Button Delete is found - TEST PASSED!")
driver.quit()

#🟦 2) EC.visibility_of_element_located
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")
wait = WebDriverWait(driver, 10)
driver.find_element(By.XPATH,"//button[text()='Start']").click()
hello_element = wait.until(EC.visibility_of_element_located((By.XPATH,"//h4[text()='Hello World!']"))).text
assert hello_element == "Hello World!"
print("2.'Hello World!' is visibility - TEST PASSED!")
driver.quit()

#🟦 3) EC.presence_of_element_located
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
wait = WebDriverWait(driver, 10)

driver.find_element(By.XPATH,"//button[text()='Start']").click()
hidden_element = wait.until(EC.presence_of_element_located((By.ID,"finish")))
print("3. hidden element is in DOM - TEST PASSED!")

#visibility test
visible_element = wait.until(EC.visibility_of_element_located((By.XPATH,"//h4[text()='Hello World!']"))).text
assert visible_element == "Hello World!"
print("4.'Hello World!' is visibility - TEST PASSED!")
driver.quit()

#🟦 5) EC.text_to_be_present_in_element
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/notification_message_rendered")
wait = WebDriverWait(driver, 10)
success= False
for i in range(5):
    driver.find_element(By.XPATH,"//a[text()='Click here']").click()
    message = wait.until(EC.visibility_of_element_located((By.ID,"flash"))).text.strip()
    print(f"attemp {i+1}: {message}")
    if "Action successful" in message:
        success = True
        break
assert success, "Không thấy message 'Action successful' sau 5 lần thử!"
print("5. 'Action successful' found — TEST PASSED!")
driver.quit()

#🟦 6) AJAX
driver = webdriver.Chrome()
driver.get("http://uitestingplayground.com/ajax")
wait = WebDriverWait(driver, 15)
try:
    driver.find_element(By.ID,"ajaxButton").click()
    msg = wait.until(EC.text_to_be_present_in_element((By.CLASS_NAME,"bg-success"),"Data loaded"))
    assert msg
    print("🎉 Test Passed: AJAX data loaded đúng!")
except TimeoutException:
    print("TEST FAILED - Timeout Error")


