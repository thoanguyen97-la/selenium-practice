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
    page.select_date_of_birth(data["dob_year"],data["dob_month"])
    page.select_hobbies()
    page.select_subject(data["subject"])
    page.upload_picture(data["picture"])
    page.fill_address(data["address"])
    page.select_state(data["state"])
    page.select_city(data["city"])
    #Step 3: Submit form
    page.submit_form()
    time.sleep(2)
    # 4. Assert kết quả
    expected_data = {
        "Student Name": "Thoa Nguyen",
        "Student Email": "thoanguyen@gmail.com",
        "Gender": "Female",
        "Mobile": "0999888777",
        "Date of Birth": "25 September,1997",
        "Subjects": "Maths",
        "Hobbies": "Reading",
        "Picture": "loopy-2.jpg",
        "Address": "123 An Duong Vuong",
        "State and City": "NCR Noida",
    }
    for label, expected_value in expected_data.items():
        actual_value= page.get_result_value(label)
        assert actual_value == expected_value,f"expected {label}: {expected_value}, but got {actual_value}"
    print("Test Passed!")






