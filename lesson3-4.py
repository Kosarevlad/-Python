def my_func(x, y):
    try:
        x, y = float(x), int(y)
        if x <= 0 or y >= 0:
            return 'x - Должен быть больше 0 а Y должен быть менбше 0'
        else:
            result = 1
            for _ in range(abs(y)):
                result /= x
            return f'Результат возведения x в степень y: {round(result, 6)}'
    except ValueError:
        return 'Введено не число'

number_1 = input('Введите х')
number_2 = input('Введите y')

print(my_func(number_1, number_2))
