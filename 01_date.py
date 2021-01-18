import time
import re


class Date:
    def __init__(self, today_date):
        self.today_date = str(today_date)

    @classmethod
    def extraction(cls, today_date):
        insert = re.compile('[0-9]+')
        # insert = re.compile('\w+')
        mass = insert.findall(today_date)
        for i, el in enumerate(mass):
            mass[i] = int(el)
        return mass

    @staticmethod
    def validation(day, month, year):
        if 0 < day <= 31:
            if 0 < month <= 12:
                if 2021 >= year > 1900:
                    return f'{day} {month} {year}'
                else:
                    return f'Год введен неверно'
            else:
                return f'Месяц введен неверно'
        else:
            return f'Число месяца введено неверно'

    def __str__(self):
        return f'Текущая дата {Date.extraction(self.today_date)}'


today = Date(time.strftime('%d-%m-%Y'))
print(today)
print(Date.extraction(time.strftime('%d-%m-%Y')))
print(Date.validation(11, 11, 2022))
print(Date.validation(11, 14, 2011))
print(Date.validation(32, 11, 2001))
