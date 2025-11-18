import os
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://demoqa.com/automation-practice-form")
wait= WebDriverWait(driver, 10)
time.sleep(3)
driver.find_element(By.ID,"firstName").send_keys("Thoa") #nhập Tên
driver.find_element(By.ID,"lastName").send_keys("Nguyễn") #nhập họ
driver.find_element(By.ID,"userEmail").send_keys("thoanguyen@gmail.com") #nhập email
#chọn giới tính
gender_ratio = wait.until(EC.presence_of_element_located((By.XPATH,"//label[text()='Female']")))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", gender_ratio)
gender_ratio.click()

driver.find_element(By.ID,"userNumber").send_keys("0987999888") #nhập SDT
#Click Calendar
driver.find_element(By.ID,"dateOfBirthInput").click()
#chọn năm
driver.find_element(By.CLASS_NAME,"react-datepicker__year-select").send_keys("1997")
#chọn tháng
driver.find_element(By.CLASS_NAME,"react-datepicker__month-select").send_keys("September")
#chọn ngày
driver.find_element(By.XPATH,"//div[contains(@class,'react-datepicker__day') and text()='25']").click()
# chờ datepicker hoàn tàn đóng lại
wait.until(EC.invisibility_of_element_located((By.CLASS_NAME,"react-datepicker")))
#driver.find_element(By.ID, "dateOfBirthInput").send_keys(Keys.ESCAPE) #đóng calendar
# scroll để chọn hobbies
hobbies_checkbox = wait.until(EC.presence_of_element_located((By.XPATH,"//label[text()='Reading']")))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", hobbies_checkbox)
hobbies_checkbox.click()
# Chọn subject (auto complete)
subject = driver.find_element(By.ID,"subjectsInput")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", subject)
subject.send_keys("math")
time.sleep(1)
subject.send_keys(Keys.ENTER)
#upload file
file_path= os.path.abspath("loopy.jpeg")
upload_button = driver.find_element(By.ID,"uploadPicture")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", upload_button)
upload_button.send_keys(file_path)
#Nhập address
address = driver.find_element(By.ID,"currentAddress")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", address)
address.send_keys("123 Ngo Quyen TP Ho Chi Minh")
#Chọn State
state = driver.find_element(By.ID,"react-select-3-input")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", state)
state.send_keys("ncr")
time.sleep(1)
state.send_keys(Keys.ENTER)
#Chọn City
city = driver.find_element(By.ID,"react-select-4-input")
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", city)
city.send_keys("noida")
time.sleep(1)
city.send_keys(Keys.ENTER)
#scroll click submit
submit_button = wait.until(EC.presence_of_element_located((By.ID,"submit")))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)
submit_button.click()
time.sleep(4)
def get_value(label):
    xpath=f"//td[text()='{label}']/following-sibling::td"
    return driver.find_element(By.XPATH,xpath).text
assert get_value("Student Name") == "Thoa Nguyễn"
assert get_value("Student Email") == "thoanguyen@gmail.com"
assert get_value("Gender") == "Female"
assert get_value("Mobile") == "0987999888"
assert get_value("Date of Birth") == "25 September,1997"
assert get_value("Subjects") == "Maths"
assert get_value("Hobbies") == "Reading"
assert get_value("Picture") == "loopy.jpeg"
assert get_value("Address") == "123 Ngo Quyen TP Ho Chi Minh"
assert get_value("State and City") == "NCR Noida"
driver.quit()

