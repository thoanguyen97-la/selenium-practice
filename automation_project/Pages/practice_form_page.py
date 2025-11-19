import os
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from automation_project.Pages.base_page import BasePage


class PracticeFormPage(BasePage):
    #URL
    URL = "https://demoqa.com/automation-practice-form"
    #LOCATORS
    FirstName = (By.ID, "firstName")
    LastName = (By.ID, "lastName")
    UserEmail = (By.ID, "userEmail")
    Gender_Female = (By.XPATH, "//label[text()='Female']")
    NumberPhone = (By.ID, "userNumber")
    DOB_Calendar = (By.ID, "dateOfBirthInput")
    DOB_Year = (By.CLASS_NAME, "react-datepicker__year-select")
    DOB_Month = (By.CLASS_NAME, "react-datepicker__month-select")
    DOB_Day_25 = (By.XPATH, "//div[contains(@class,'react-datepicker__day') and text()='25']")
    DatePicker = (By.CLASS_NAME, "react-datepicker")
    Hobbies = (By.XPATH, "//label[text()='Reading']")
    Subject = (By.ID, "subjectsInput")
    Picture = (By.ID, "uploadPicture")
    Address = (By.ID, "currentAddress")
    State = (By.ID, "react-select-3-input")
    City = (By.ID, "react-select-4-input")
    Submit_Button = (By.ID, "submit")
    Result_Value = (By.XPATH, "//td[text()='{label}']/following-sibling::td")

    #fill basic info
    def fill_basic_info(self,first_name, last_name, email, phone_number):
        self.type(self.FirstName,first_name)
        self.type(self.LastName,last_name)
        self.type(self.UserEmail,email)
        self.type(self.NumberPhone,phone_number)
    #chọn gender = female
    def select_gender(self):
        female = self.find_element(self.Gender_Female)
        self.scroll_into_view(female)
        self.click(self.Gender_Female)
    #Chọn date of birth
    def select_date_of_birth(self, year: str,month: str):
        #clcik calendar
        dob_input = self.find_element(self.DOB_Calendar)
        self.scroll_into_view(dob_input)
        self.click(dob_input)
        #select year
        self.type(self.DOB_Year,year)
        #select month
        self.type(self.DOB_Month,month)
        #select day
        self.find_element(self.DOB_Day_25)
        self.click(self.DOB_Day_25)
        #chờ date picker invisibility để không che mất những element bên dưới
        self.wait_invisibility(self.DatePicker)
    # Select Hobbies
    def select_hobbies(self):
        hobbies= self.find_element(self.Hobbies)
        self.scroll_into_view(hobbies)
        self.click(hobbies)
    #select Subject
    def select_subject(self, subject_text: str):
        subject = self.find_element(self.Subject)
        self.scroll_into_view(subject)
        self.type(self.Subject, subject_text)
        time.sleep(1)
        subject.send_keys(Keys.ENTER)
    #upload picture
    def upload_picture(self, filename: str):
        base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        full_path = os.path.join(base, "resources", filename)
        upload = self.find_element(self.Picture)
        self.scroll_into_view(upload)
        upload.send_keys(full_path)
    #Type address
    def fill_address(self, address_text: str):
        address = self.find_element(self.Address)
        self.scroll_into_view(address)
        address.send_keys(address_text)
    #Select State
    def select_state(self, state_text: str):
        state = self.find_element(self.State)
        self.scroll_into_view(state)
        state.send_keys(state_text)
        time.sleep(1)
        state.send_keys(Keys.ENTER)
    #Select City
    def select_city(self, city_text: str):
        city = self.find_element(self.City)
        self.scroll_into_view(city)
        city.send_keys(city_text)
        time.sleep(1)
        city.send_keys(Keys.ENTER)
    #Submit form
    def submit_form(self):
        submit_button = self.find_element(self.Submit_Button)
        self.scroll_into_view(submit_button)
        self.click(submit_button)
    #Get Result Value
    def get_result_value(self,label):
        xpath = f"//td[text()='{label}']/following-sibling::td"
        return self.find_element((By.XPATH, xpath)).text

















