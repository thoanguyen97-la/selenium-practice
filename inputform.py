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
#scroll click submit
submit_button = wait.until(EC.presence_of_element_located((By.ID,"submit")))
driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_button)
submit_button.click()
time.sleep(4)
driver.quit()
