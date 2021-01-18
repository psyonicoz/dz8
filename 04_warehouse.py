import json


class Warehouse:
    def work_hours(self):
        pass

    def free_space(self):
        pass


class OfficeEquipment:
    def __init__(self, *args):
        self.dict = {'model': '', 'price': '', 'quantity': ''}

    def __str__(self):
        return f'{self.dict}'

    def wh_selection(self):
        def inner(func):
            wh_numb = int(input('Введите номер склада '))
            while True:
                with open(f'{wh_numb}.json', 'a+', encoding="utf-8") as file:
                    json.dump(self(func), file)
                a = input('Для остановки ввода наберите stop, '
                          'для продолжения нажмите Enter ')
                if a.lower() == 'stop':
                    break
        return inner

    @wh_selection
    def accepatance(self):
        for key in self.dict.keys():
            if key == 'model':
                self.dict[key] = input('Введите модель ')
            elif key == 'price':
                while True:
                    try:
                        self.dict[key] = int(input('Введите цену за ед. '))
                        break
                    except ValueError:
                        print('Введите число ')
            elif key == 'quantity':
                while True:
                    try:
                        self.dict[key] = int(input('Введите количество ед. '))
                        break
                    except ValueError:
                        print('Введите число ')
        return self.dict


class Printer(OfficeEquipment):
    def print_speed(self, speed):
        self.speed = speed
        return f'Скорость печати {self.speed} страниц в минуту'


class Scanner(OfficeEquipment):
    def scan_speed(self, speed):
        self.speed = speed
        return f'Скорость сканирования {self.speed} страниц в минуту'


class Xerox(OfficeEquipment):
    def copy_speed(self, speed):
        self.speed = speed
        return f'Скорость копирокания {self.speed} страниц в минуту'


d = OfficeEquipment()
d.accepatance()
