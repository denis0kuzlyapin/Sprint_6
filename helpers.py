import random


RUSSIAN_LETTERS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
RUSSIAN_CAPITAL = RUSSIAN_LETTERS.capitalize()

class DataForOrder:
    
    
    @staticmethod
    def gen_name():
        first = random.choice(RUSSIAN_CAPITAL)
        rest = ''.join(random.choices(RUSSIAN_LETTERS, k=6))
        return first + rest
    
    @staticmethod
    def gen_last_name():
        first = random.choice(RUSSIAN_CAPITAL)
        rest = ''.join(random.choices(RUSSIAN_LETTERS, k=7))
        return first + rest
    
    @staticmethod
    def gen_delivery_address():  
        first = random.choice(RUSSIAN_CAPITAL)
        rest = ''.join(random.choices(RUSSIAN_LETTERS, k=20))
        return first + rest
    
    @staticmethod
    def gen_phone_number():
        phone_number = str(random.randint(11111111111, 99999999999))
        return phone_number
    
    @staticmethod
    def gen_comment():  
        first = random.choice(RUSSIAN_CAPITAL)
        rest = ''.join(random.choices(RUSSIAN_LETTERS, k=30))
        return first + rest