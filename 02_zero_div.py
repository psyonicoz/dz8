class ZeroDivisionError(Exception):
    def __init__(self, number):
        self.number = number


digit_1 = int(input('Введите делимое '))
digit_2 = int(input('Введите делитель '))

try:
    if digit_2 == 0:
        raise ZeroDivisionError('Деление на ноль запрещено')
    else:
        print(f'{digit_1 / digit_2:.02}')
except ZeroDivisionError as e:
    print(e)
