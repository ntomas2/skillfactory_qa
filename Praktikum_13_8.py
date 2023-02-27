# Практикум 13.8
def check_number(text):
    while True:
        try:
            number = int(input(text))
            if number <= 0:
                raise ValueError
            break
        except ValueError:
            print('Вы ввели некорректное значение!')
    return number


tickets = check_number('Введите количество билетов: ')
prices = 0
for _ in range(tickets):
    age = check_number('Введите возраст участника: ')
    if age < 18:
        continue
    elif 18 <= age < 25:
        prices += 990
    else:
        prices += 1390
print(f'К оплате: {prices if tickets <= 3 else prices * 0.9}')
