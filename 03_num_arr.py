class NotANumber(Exception):
    def __init__(self, number):
        self.number = number


arr = []

while True:
    try:
        insert = input('Введите число: ')
        if not insert.isdigit():
            raise NotANumber(f'Необходимо вводить только числа')
        arr.append(int(insert))
        print(f'{arr}')
    except NotANumber as e:
        print(e)
        insert = input(f'Чтобы закончить, введите stop: ')
        if insert.lower() == 'stop':
            print(f'{arr}')
            break
