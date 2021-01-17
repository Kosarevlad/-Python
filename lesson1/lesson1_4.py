
num = int(input('Введите любое число:'))
x = 0
while True:
    y = (num % 10)
    if num // 10 == 0:
        if y >= x:
            x = y
            break
        if y < x:
            break
    if y >= x and num // 10 != 0:
        x = y
        num = num // 10
        continue
    if y < x:
        num = num // 10
        continue
print('Наибольшее число:', x)