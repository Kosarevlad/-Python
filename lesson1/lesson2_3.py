x = int(input('Введите число месяца:'))

winter = [12,1,2]
spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]

if winter.count(x) == 1:
    print('Решение через list:', 'winter')
if spring.count(x) == 1:
    print('Решение через list:', 'spring')
if summer.count(x) == 1:
    print('Решение через list:', 'summer')
if autumn.count(x) == 1:
    print('Решение через list:', 'autumn')
if winter.count(x) == spring.count(x) == summer.count(x) == autumn.count(x):
    print('Решение через list:', 'Введите значение от 1 до 12')

#------------------------------------------------------------------


my_dict = {12: 'winter', 1: 'winter', 2: 'winter', 3: 'spring', 4: 'spring', 5: 'spring', 6: 'summer', 7: 'summer', 8: 'summer', 9: 'autumn', 10: 'autumn', 11: 'autumn'}

print('Решение через dict:', my_dict.get(x))

if x >= 12:
    print('Решение через dict:', 'Введите значение от 1 до 12')
if x <= 1:
    print('Решение через dict:', 'Введите значение от 1 до 12')
