from selenium import webdriver
from selenium.webdriver.common.by import By
import os

driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/upload")

# 1️⃣ Chuẩn bị đường dẫn file tuyệt đối
file_path = os.path.abspath("myfile.txt")
print("print file path:",file_path)

# 2️⃣ Upload file bằng send_keys()
upload_input = driver.find_element(By.ID,"file-upload")
upload_input.send_keys(file_path)

# 3️⃣ Click Upload button
driver.find_element(By.ID,"file-submit").click()

# 4️⃣ Assert kết quả

success_msg = driver.find_element(By.XPATH,"//h3[text()='File Uploaded!']").text
file_name = driver.find_element(By.ID,"uploaded-files").text
assert success_msg == "File Uploaded!"
assert file_name == "myfile.txt"
print("✅ Upload file passed!")
driver.quit()





