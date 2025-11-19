class PracticeFormPage(BasePage):

    first_name = (By.ID, "firstName")
    last_name = (By.ID, "lastName")
    email = (By.ID, "userEmail")
    phone = (By.ID, "userNumber")
    subjects = (By.ID, "subjectsInput")
    address = (By.ID, "currentAddress")
    submit = (By.ID, "submit")