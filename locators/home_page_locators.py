from selenium.webdriver.common.by import By

class FAQ:
    
    how_much_does_it_cost_dd = [By.XPATH,"//div[@id='accordion__heading-0']/parent::div"]

    i_want_several_scooters_at_once_dd = [By.XPATH,"//div[@id='accordion__heading-1']/parent::div"]

    how_is_rental_time_calculated_dd = [By.XPATH,"//div[@id='accordion__heading-2']/parent::div"]

    can_i_order_for_today_dd = [By.XPATH,"//div[@id='accordion__heading-3']/parent::div"]

    can_i_extend_or_return_earlier_dd = [By.XPATH,"//div[@id='accordion__heading-4']/parent::div"]

    do_you_bring_charger_dd = [By.XPATH,"//div[@id='accordion__heading-5']/parent::div"]

    can_i_cancel_order_dd = [By.XPATH,"//div[@id='accordion__heading-6']/parent::div"]

    do_you_deliver_outside_mkad_dd = [By.XPATH,"//div[@id='accordion__heading-7']/parent::div"]
    
    
class FAQAnswer:
    
    how_much_does_it_cost_answer = [By.XPATH,"//div[@id='accordion__panel-0']/p"]
    
    i_want_several_scooters_at_once_answer = [By.XPATH,"//div[@id='accordion__panel-1']/p"]
    
    how_is_rental_time_calculated_answer = [By.XPATH,"//div[@id='accordion__panel-2']/p"]
    
    can_i_order_for_today_answer = [By.XPATH,"//div[@id='accordion__panel-3']/p"]
    
    can_i_extend_or_return_earlier_answer = [By.XPATH,"//div[@id='accordion__panel-4']/p"]
    
    do_you_bring_charger_answer = [By.XPATH,"//div[@id='accordion__panel-5']/p"]
    
    can_i_cancel_order_answer = [By.XPATH,"//div[@id='accordion__panel-6']/p"]
    
    do_you_deliver_outside_mkad_answer = [By.XPATH,"//div[@id='accordion__panel-7']/p"]