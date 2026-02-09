import allure
from pages.base_page import BasePage
from constants import TestingPages
from locators.home_page_locators import FAQ


class HomePage(BasePage):

    @allure.step("Открываем тестируемую страницу приложения")
    def open_page(self):
        self.driver.get(TestingPages.HOME_PAGE_SCOOTER)

    @allure.step("Скроллим страницу вниз до блока FAQ")
    def scroll_down(self):
        self.driver.execute_script(
            "arguments[0].scrollIntoView();", self.driver.find_element(*FAQ.do_you_deliver_outside_mkad_dd)
        )

    @allure.step("Кликаем по вопросу FAQ")
    def click_faq_locator(self, faq_locator):
        self.click(faq_locator)

    @allure.step("Читаем текст ответа FAQ")
    def get_faq_locator_answer_txt(self, faq_locator_answer):
        return self.get_text(faq_locator_answer)
