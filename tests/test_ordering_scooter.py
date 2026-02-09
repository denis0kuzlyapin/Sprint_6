import pytest
import allure

from constants import TestingPages
from pages.order_scooter_page import OrderScooterPage
from locators.order_scooter_page_locator import (
    OrderBtn,
    OrderFormPersonalData,
    OrderFormScooterData,
)


@allure.title("Оформление заказа самоката через две точки входа")
@allure.description(
    "Сквозной параметризованный кейс: заказ самоката через верхнюю и нижнюю кнопки"
)
@pytest.mark.parametrize(
    "order_btn, metro_station, date, lease_period, color",
    [
        (
            OrderBtn.order_upper_btn,
            OrderFormPersonalData.second_metro_station,
            OrderFormScooterData.eleven_day,
            OrderFormScooterData.one_day_dd,
            OrderFormScooterData.color_black_pearl_cb,
        ),
        (
            OrderBtn.order_lower_btn,
            OrderFormPersonalData.third_metro_station,
            OrderFormScooterData.twelve_day,
            OrderFormScooterData.two_day_dd,
            OrderFormScooterData.color_gray_despair_cb,
        ),
    ],
)
class TestOrderingScooter:

    def test_order_scooter_flow(
        self, driver, order_btn, metro_station, date, lease_period, color
    ):
        order_scooter_page = OrderScooterPage(driver)

        order_scooter_page.open_page()

        if order_btn is OrderBtn.order_lower_btn:
            order_scooter_page.scroll_down()

        order_scooter_page.click_order(order_btn)
        order_scooter_page.fill_order_form_personal_data(metro_station)
        order_scooter_page.fill_order_form_data_scooter(date, lease_period, color)

        order_scooter_page.wait_successfully_issued_modal()
        order_scooter_page.wait_check_status()
        order_scooter_page.click_check_status()
        order_scooter_page.click_logo_scooter()

        assert order_scooter_page.get_current_url() == TestingPages.ORDER_SCOOTER_PAGE

        order_scooter_page.click_logo_yandex()

        assert order_scooter_page.get_current_url() == TestingPages.YANDEX_DZEN_PAGE
