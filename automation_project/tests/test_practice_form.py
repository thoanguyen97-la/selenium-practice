import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from automation_project.Pages.practice_form_page import PracticeFormPage
from automation_project.utils.data_loader import load_json

def test_input_practice_form():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    page = PracticeFormPage(driver) #tạo object
    #Step 1: Open Form
    page.open(page.URL) #mở browser
    #step 2: fill information
    data = load_json("test_data.json")["student"]
    page.fill_basic_info(
        data["first_name"],
        data["last_name"],
        data["email"],
        data["phone"]
    )
    page.select_gender()
    page.select_date_of_birth("1997","September")
    page.select_hobbies()
    page.select_subject("math")
    page.upload_picture("loopy-2.jpg")
    page.fill_address(data["address"])
    page.select_state("NCR")
    page.select_city("Noida")
    #Step 3: Submit form
    page.submit_form()
    time.sleep(2)
    # 4. Assert kết quả
    assert page.get_result_value("Student Name") == "Thoa Nguyen"
    assert page.get_result_value("Student Email") == "thoanguyen@gmail.com"
    assert page.get_result_value("Gender") == "Female"
    assert page.get_result_value("Mobile") == "0999888777"
    assert page.get_result_value("Date of Birth") == "25 September,1997"
    assert page.get_result_value("Subjects") == "Maths"
    assert page.get_result_value("Hobbies") == "Reading"
    assert page.get_result_value("Picture") == "loopy-2.jpg"
    assert page.get_result_value("Address") == "123 An Duong Vuong"
    assert page.get_result_value("State and City") == "NCR Noida"
    print("Test Passed!")






