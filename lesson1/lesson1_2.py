sek = int(input('Число секунд:'))
H = sek // 3600
M = (sek - H * 3600) // 60
S = (sek - H * 3600 - M * 60)
print(f'Полученный результат - {H:02d}:{M:02d}:{S:02d}')