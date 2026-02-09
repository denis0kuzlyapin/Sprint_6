import allure
from constants import TestingPages
from helpers import DataForOrder
from locators.order_scooter_page_locator import (
    OrderFormPersonalData,
    OrderFormScooterData,
    ModelOrderSuccessfullyCreated,
    HeaderLogo,
)
from pages.base_page import BasePage


class OrderScooterPage(BasePage):

    @allure.step("Открываем тестируемую страницу приложения")
    def open_page(self):
        self.driver.get(TestingPages.HOME_PAGE_SCOOTER)

    @allure.step("Нажимаем кнопку 'Заказать'")
    def click_order(self, order_btn):
        self.click(order_btn)

    @allure.step("Скроллим страницу вниз")
    def scroll_down(self):
        super().scroll_down()

    @allure.step("Вводим имя")
    def set_name(self):
        self.send_keys(OrderFormPersonalData.name_input, DataForOrder.gen_name())

    @allure.step("Вводим фамилию")
    def set_last_name(self):
        self.send_keys(
            OrderFormPersonalData.last_name_input, DataForOrder.gen_last_name()
        )

    @allure.step("Вводим адрес доставки")
    def set_delivery_address(self):
        self.send_keys(
            OrderFormPersonalData.delivery_address_input,
            DataForOrder.gen_delivery_address(),
        )

    @allure.step("Открываем список станций метро")
    def click_dropdown_metro_station(self):
        self.click(OrderFormPersonalData.metro_station_dd)

    @allure.step("Выбираем станцию метро")
    def select_metro_station(self, metro_station):
        self.click(metro_station)

    @allure.step("Вводим номер телефона")
    def set_phone_number(self):
        self.send_keys(
            OrderFormPersonalData.phone_number_input, DataForOrder.gen_phone_number()
        )

    @allure.step("Нажимаем кнопку 'Далее'")
    def click_forth_btn(self):
        self.click(OrderFormPersonalData.forth_btn)

    @allure.step("Заполнить форму с персональными данными")
    def fill_order_form_personal_data(self, metro_station):
        self.set_name()
        self.set_last_name()
        self.set_delivery_address()
        self.click_dropdown_metro_station()
        self.select_metro_station(metro_station)
        self.set_phone_number()
        self.click_forth_btn()

    @allure.step("Нажимаем на дропдаун с календарем")
    def click_dropdown_date(self):
        self.click(OrderFormScooterData.date_input)

    @allure.step("Выбираем дату в календаре")
    def select_date(self, date):
        self.click(date)

    @allure.step("Нажимаем на дропдаун со сроками аренды")
    def click_dropdown_lease_period(self):
        self.click(OrderFormScooterData.lease_period_dd)

    @allure.step("Ждем появления списка сроков аренды")
    def wait_dropdown_lease_period(self):
        self.wait_visible(OrderFormScooterData.list_periods)

    @allure.step("Выбираем срок аренды")
    def select_lease_period(self, lease_period):
        self.click(lease_period)

    @allure.step("Выбираем цвет самоката")
    def select_color(self, color):
        self.click(color)

    @allure.step("Вводим комментарий к заказу")
    def set_comment(self):
        self.send_keys(OrderFormScooterData.comment_input, DataForOrder.gen_comment())

    @allure.step("Нажимаем кнопку 'Заказать' на второй форме")
    def click_order_finish(self):
        self.click(OrderFormScooterData.order_finish_btn)

    @allure.step("Ждем кнопки подтверждения заказа")
    def wait_confirm_btn(self):
        self.wait_visible(OrderFormScooterData.confirm_btn)

    @allure.step("Подтверждаем заказ")
    def click_yes(self):
        self.click(OrderFormScooterData.confirm_btn)

    @allure.step("Заполнить форму с данными о самокате и времени")
    def fill_order_form_data_scooter(self, date, lease_period, color):
        self.click_dropdown_date()
        self.select_date(date)
        self.click_dropdown_lease_period()
        self.wait_dropdown_lease_period()
        self.select_lease_period(lease_period)
        self.select_color(color)
        self.set_comment()
        self.click_order_finish()
        self.wait_confirm_btn()
        self.click_yes()

    @allure.step("Ждем окно 'Заказ оформлен'")
    def wait_successfully_issued_modal(self):
        self.wait_visible(ModelOrderSuccessfullyCreated.successfully_issued)

    @allure.step("Ждем появления кнопки 'Посмотреть статус'")
    def wait_check_status(self):
        self.wait_visible(ModelOrderSuccessfullyCreated.checking_status_btn)

    @allure.step("Нажимаем кнопку 'Посмотреть статус'")
    def click_check_status(self):
        self.click(ModelOrderSuccessfullyCreated.checking_status_btn)

    @allure.step("Кликаем по лого Самокат")
    def click_logo_scooter(self):
        self.click(HeaderLogo.header_logo_scooter)

    @allure.step("Получаем текущий URL страницы")
    def get_current_url(self):
        return super().get_current_url()

    @allure.step("Кликаем по лого Яндекс и переходим на главную страницу 'Дзен'")
    def click_logo_yandex(self):
        self.click(HeaderLogo.header_logo_yandex)
        self.switch_to_new_tab_and_wait_url(TestingPages.YANDEX_DZEN_PAGE)
