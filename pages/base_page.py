from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver,timeout=10):
        self.driver = driver
        self.wait= WebDriverWait(driver,timeout)
    def open(self):
        self.driver.get(self.driver.current_url)