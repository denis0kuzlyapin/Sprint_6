from constants import TestingPages
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class HomePage():
    def __init__(self,driver):
        self.driver = driver
        
    def open_page(self):
        self.driver.get(TestingPages.HOME_PAGE_SCOOTER)

    def click_faq_locator(self,faq_locator):
        self.driver.find_element(*faq_locator).click()
        
    
    def get_faq_locator_answer_txt(self, faq_locator_answer):
        text_answer = WebDriverWait(self.driver, 5).until(
            expected_conditions.visibility_of_element_located(faq_locator_answer)
        )
        return text_answer.text
    
