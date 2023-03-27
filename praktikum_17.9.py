def qsort(array, left, right):
    middle = (left + right) // 2

    p = array[middle]
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort(array, left, j)
    if right > i:
        qsort(array, i, right)
    return array


def binary_search(array, element, left, right):
    try:
        if left > right:
            return False
        middle = (right + left) // 2
        if array[middle] == element:
            return middle
        elif element < array[middle]:
            return binary_search(array, element, left, middle - 1)
        else:
            return binary_search(array, element, middle + 1, right)
    except IndexError:
        return 'Число выходит за диапазон списка, введите меньшее число.'


nums = [int(x) for x in input().split()]
user_input = int(input())
nums = qsort(nums, 0, len(nums) - 1)

if not binary_search(nums, user_input, 0, len(nums) - 1):
    rI = min(nums, key=lambda x: (abs(x - user_input), x))
    ind = nums.index(rI)
    max_ind = ind + 1
    min_ind = ind - 1
    if rI < user_input:
        print(f'''В списке нет введенного элемента 
Ближайший меньший элемент: {rI}, его индекс: {ind}
Ближайший больший элемент: {nums[max_ind]} его индекс: {max_ind}''')
    elif min_ind < 0:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {nums.index(rI)}
В списке нет меньшего элемента''')
    elif rI > user_input:
        print(f'''В списке нет введенного элемента
Ближайший больший элемент: {rI}, его индекс: {nums.index(rI)}
Ближайший меньший элемент: {nums[min_ind]} его индекс: {min_ind}''')
    elif nums.index(rI) == 0:
        print(f'Индекс введенного элемента: {nums.index(rI)}')
else:
    print(f'Индекс введенного элемента: {binary_search(nums, user_input, 0, len(nums))}')
