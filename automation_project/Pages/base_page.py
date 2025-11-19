from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import Tuple
Locator = Tuple[str, str]
class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    #mở browser
    def open(self, url: str):
        self.driver.get(url)
    #đóng browser
    def close(self):
        self.driver.quit()
    #tìm element
    def find_element(self, locator: Locator):
        return self.wait.until(EC.presence_of_element_located(locator))
    #hàm click
    def click(self, locator: Locator):
        el = self.wait.until(EC.element_to_be_clickable(locator))
        el.click()
        return el
    #hàm nhập
    def type(self, locator: Locator, text: str):
        el = self.find_element(locator)
        el.send_keys(text)
        return el
    #scroll into View
    def scroll_into_view(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",element)
    #wait handling
    def wait_invisibility(self, locator: Locator):
        self.wait.until(EC.invisibility_of_element_located(locator))

