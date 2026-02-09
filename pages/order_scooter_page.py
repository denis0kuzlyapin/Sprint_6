from constants import TestingPages
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helpers import DataForOrder
from locators.order_scooter_page_locator import (OrderFormPersonalData, OrderFormScooterData, ModelOrderSuccessfullyCreated, HeaderLogo)
import time

class OrderScooterPage():
    def __init__(self,driver):
        self.driver = driver
        
    def open_page(self):
        self.driver.get(TestingPages.HOME_PAGE_SCOOTER)
        
#Нажать кнопку «Заказать». На странице две кнопки заказа.    
    def click_order(self,order_btn):
        self.driver.find_element(*order_btn).click()
        
    def set_name(self):
        self.driver.find_element(*OrderFormPersonalData.name_input).send_keys(DataForOrder.gen_name())
        
    def set_last_name(self):
        self.driver.find_element(*OrderFormPersonalData.last_name_input).send_keys(DataForOrder.gen_last_name())
        
    def set_delivery_address(self):
        self.driver.find_element(*OrderFormPersonalData.delivery_address_input).send_keys(DataForOrder.gen_delivery_address())

    #Нажимаем на дропдаун со станциями метро
    def click_dropdown_metro_station(self):
        self.driver.find_element(*OrderFormPersonalData.metro_station_dd).click()
    #Выбираем станцию метро из выпадающего списка
    def select_metro_station(self,metro_station):
        self.driver.find_element(*metro_station).click()

    def set_phone_number(self):
        self.driver.find_element(*OrderFormPersonalData.phone_number_input).send_keys(DataForOrder.gen_phone_number())

    #Нажимаем на дкнопку "Далее"
    def click_forth_btn(self):
        self.driver.find_element(*OrderFormPersonalData.forth_btn).click()
    
    #Заполнить и отпрвить форму заказа с персональными данными
    def fill_order_form_personal_data(self,metro_station):
        self.set_name()
        self.set_last_name()
        self.set_delivery_address()
        self.click_dropdown_metro_station()
        self.select_metro_station(metro_station)
        self.set_phone_number()
        self.click_forth_btn()
     
     
    def click_dropdown_date(self):
        self.driver.find_element(*OrderFormScooterData.date_input).click()

    def select_date(self,date):
        self.driver.find_element(*date).click()
        
    def click_dropdown_lease_period(self):
        self.driver.find_element(*OrderFormScooterData.lease_period_dd).click()
        
    def wait_dropdown_lease_period(self):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(OrderFormScooterData.list_periods))
        
    def select_lease_period(self,lease_period):
        self.driver.find_element(*lease_period).click()
        
    def select_color(self,color):
         self.driver.find_element(*color).click()
        
    def set_comment(self):
        self.driver.find_element(*OrderFormScooterData.comment_input).send_keys(DataForOrder.gen_comment())
    
    def click_order_finish(self):
        self.driver.find_element(*OrderFormScooterData.order_finish_btn).click()   
        
    def wait_confirm_btn(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(OrderFormScooterData.confirm_btn))
            
    def click_yes(self):
        self.driver.find_element(*OrderFormScooterData.confirm_btn).click() 
        
        
    #Заполнить и отпрвить форму заказа данными о самокате и времени
    def fill_order_form_data_scooter(self,date,lease_period,color):
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
        

    def wait_successfully_issued_modal(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(ModelOrderSuccessfullyCreated.successfully_issued))
        
    def wait_check_status(self):
        WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(ModelOrderSuccessfullyCreated.checking_status_btn))
        
    def click_check_status(self):
        self.driver.find_element(*ModelOrderSuccessfullyCreated.checking_status_btn).click() 
    
        
    def click_logo_scooter(self):
        self.driver.find_element(*HeaderLogo.header_logo_scooter).click() 
        
    def click_logo_yandex(self):
        # клик по лого "Яндекс"
        self.driver.find_element(*HeaderLogo.header_logo_yandex).click()

        # ждём появления новой вкладки
        WebDriverWait(self.driver, 15).until(
            lambda d: len(d.window_handles) > 1
        )

        # переключаемся на новую вкладку
        new_tab = self.driver.window_handles[-1]
        self.driver.switch_to.window(new_tab)

        time.sleep(3)