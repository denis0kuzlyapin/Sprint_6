import pytest
import allure

from pages.home_page import HomePage
from constants import FAQAnswerText
from locators.home_page_locators import FAQ, FAQAnswer


class TestDropdownFAQ:

    FAQ_DATA = [
        (
            FAQ.how_much_does_it_cost_dd,
            FAQAnswer.how_much_does_it_cost_answer,
            FAQAnswerText.FAQ_HOW_MUCH_DOES_IT_COST,
        ),
        (
            FAQ.i_want_several_scooters_at_once_dd,
            FAQAnswer.i_want_several_scooters_at_once_answer,
            FAQAnswerText.FAQ_I_WANT_SEVERAL_SCOOTERS,
        ),
        (
            FAQ.how_is_rental_time_calculated_dd,
            FAQAnswer.how_is_rental_time_calculated_answer,
            FAQAnswerText.FAQ_RENTAL_TIME_CALCULATED,
        ),
        (
            FAQ.can_i_order_for_today_dd,
            FAQAnswer.can_i_order_for_today_answer,
            FAQAnswerText.FAQ_CAN_I_ORDER_FOR_TODAY,
        ),
        (
            FAQ.can_i_extend_or_return_earlier_dd,
            FAQAnswer.can_i_extend_or_return_earlier_answer,
            FAQAnswerText.FAQ_CAN_I_EXTEND_OR_RETURN_EARLIER,
        ),
        (
            FAQ.do_you_bring_charger_dd,
            FAQAnswer.do_you_bring_charger_answer,
            FAQAnswerText.FAQ_DO_YOU_BRING_CHARGER,
        ),
        (
            FAQ.can_i_cancel_order_dd,
            FAQAnswer.can_i_cancel_order_answer,
            FAQAnswerText.FAQ_CAN_I_CANCEL_ORDER,
        ),
        (
            FAQ.do_you_deliver_outside_mkad_dd,
            FAQAnswer.do_you_deliver_outside_mkad_answer,
            FAQAnswerText.FAQ_DO_YOU_DELIVER_OUTSIDE_MKAD,
        ),
    ]

    @allure.title("Проверка ответов на FAQ")
    @allure.description(
        "Параметризованный тест: проверка текста ответа после клика по дропдауну FAQ"
    )
    @pytest.mark.parametrize("faq_locator, faq_locator_answer, expected_text", FAQ_DATA)
    def test_check_answer_to_question(
        self, driver, faq_locator, faq_locator_answer, expected_text
    ):
        home_page = HomePage(driver)

        home_page.open_page()
        home_page.scroll_down()
        home_page.click_faq_locator(faq_locator)

        actual_text = home_page.get_faq_locator_answer_txt(faq_locator_answer)

        assert actual_text == expected_text
