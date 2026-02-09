from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def click(self, locator):
        self.wait.until(expected_conditions.element_to_be_clickable(locator)).click()

    def send_keys(self, locator, value):
        self.wait.until(
            expected_conditions.visibility_of_element_located(locator)
        ).send_keys(value)

    def get_text(self, locator):
        return self.wait.until(
            expected_conditions.visibility_of_element_located(locator)
        ).text

    def wait_visible(self, locator):
        self.wait.until(expected_conditions.visibility_of_element_located(locator))

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def get_current_url(self):
        return self.driver.current_url

    def switch_to_new_tab_and_wait_url(self, url_substring, timeout=None):
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        # Ждем появления второй вкладки
        wait.until(lambda d: len(d.window_handles) > 1)
        # Переключаемся на последнюю вкладку
        self.driver.switch_to.window(self.driver.window_handles[-1])
        # Ждем, пока URL новой вкладки будет содержать нужную подстроку
        wait.until(expected_conditions.url_contains(url_substring))
