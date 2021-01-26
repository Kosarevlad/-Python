x = [9, 8, 7, 6, 5, 4, 3, 2, 1]
y = int(input('Введите число:'))
z = 0
for n in x:
    if y <= n:
        z += 1
x.insert(z, y)
print(x)