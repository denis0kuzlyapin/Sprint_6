from selenium.webdriver.common.by import By

class OrderBtn:
    #Верхняя кнопка "Заказать"
    order_upper_btn = [By.XPATH, "(//button[contains(@class,'Button_Button__ra12g') and text()='Заказать'])[1]"]
    #Нижняя кнопка "Заказать"
    order_lower_btn = [By.XPATH, "(//button[contains(@class,'Button_Button__ra12g') and text()='Заказать'])[2]"]


class OrderFormPersonalData:
   
    #Заполнить форму заказа.
    #Инпут с именем
    name_input =  [By.XPATH, "//input[@placeholder='* Имя']"]
    #Инпут с фамилией
    last_name_input = [By.XPATH, "//input[@placeholder='* Фамилия']"]
    #Инпут с адресом доставки
    delivery_address_input = [By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"]
    #Дроп-даун со станциями метро
    metro_station_dd = [By.XPATH, "//input[@placeholder='* Станция метро']"]
    #Вторая станция метро из дроп-дауна
    second_metro_station = [By.XPATH, "//button[@class ='Order_SelectOption__82bhS select-search__option' and @value= '2']"]
    #Третья станция метро из дроп-дауна
    third_metro_station = [By.XPATH, "//button[@class ='Order_SelectOption__82bhS select-search__option' and @value= '3']"]
    #Инпут с номер телефона
    phone_number_input = [By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"]
    #Кнопка "Далее"
    forth_btn = [By.XPATH, "//button[contains(@class,'Button_Button__ra12g') and text()='Далее']"]


class OrderFormScooterData:
    
    #Инпут для даты
    date_input =  [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    #11 число любого месяца
    eleven_day = [By.XPATH, "//div[@class ='react-datepicker__day react-datepicker__day--011']"]
    #12 число любого месяца
    twelve_day = [By.XPATH, "//div[@class ='react-datepicker__day react-datepicker__day--012']"]
    #Дроп-даун срока аренды
    lease_period_dd = [By.XPATH, "//div[contains(@class,'Dropdown-placeholder') and text()='* Срок аренды']"]
    #Список со сроками
    list_periods = [By.XPATH, "//div[@class='Dropdown-menu' and @aria-expanded= 'true']"]
    #Срок аренды: "сутки"
    one_day_dd = [By.XPATH, "//div[contains(@class,'Dropdown-option') and text()='сутки']"]
    #Срок аренды: "двое суток"
    two_day_dd = [By.XPATH, "//div[contains(@class,'Dropdown-option') and text()='двое суток']"]
    #Чек-бокс "чёрный жемчуг"
    color_black_pearl_cb = [By.XPATH, "//label[@class ='Checkbox_Label__3wxSf' and @for= 'black']"]
    #Чек-бокс "серая безысходность"
    color_gray_despair_cb = [By.XPATH, "//label[@class ='Checkbox_Label__3wxSf' and @for= 'grey']"]
    #Инпут для комментария курьеру
    comment_input = [By.XPATH, "//input[@placeholder='* Когда привезти самокат']"]
    #Кнопка "Заказать"
    order_finish_btn = [By.XPATH,"//button[contains(@class,'Button_Button__ra12g Button_Middle__1CSJM') and text()='Заказать']"]
    #Кнопка "Да" в модалке с подтверждением
    confirm_btn = [By.XPATH, "//button[contains(@class,'Button_Button__ra12g') and contains(@class,'Button_Middle__1CSJM') and text()='Да']"]


class ModelOrderSuccessfullyCreated:
    
    #Модалка с сообщением об успешном создании заказа
    successfully_issued = [By.XPATH, "//div[contains(@class,'Order_ModalHeader__3FDaJ') and text()='Заказ оформлен']"]
    #Кнопка "Посмотреть статус"
    checking_status_btn = [By.XPATH, "//button[contains(@class,'Button_Button__ra12g') and contains(@class,'Button_Middle__1CSJM') and text()='Посмотреть статус']"]
    
class HeaderLogo:    
    #Кнопка для перехода на главную страницу «Самоката»
    header_logo_scooter = [By.XPATH, "//a[@class= 'Header_LogoScooter__3lsAR']"]
    #Кнопка для перехода на главную страницу Дзена
    header_logo_yandex = [By.XPATH, "//a[@class= 'Header_LogoYandex__3TSOI']"]