# Практикум 12.7

# Процентные ставки в разных банках
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
# Сумма вклада
money = int(input())
# Список накопленных средств за год вклада в каждом банке
deposit = [money * interest_rate * 0.01 for interest_rate in per_cent.values()]
print(f'Максимальная сумма, которую вы можете заработать — {max(deposit)}')
