from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.home_page_locators import FAQ


class BaseMethods:
    @staticmethod
    def scroll_down(driver):
        last_faq = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located(FAQ.do_you_deliver_outside_mkad_dd)
        )
        driver.execute_script("arguments[0].scrollIntoView();", last_faq)

    @staticmethod
    def get_current_url(driver):
        return driver.current_url