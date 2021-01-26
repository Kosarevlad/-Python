z = input('Введите несколько слок разделенных пробелами:')

for ind, el in enumerate(str(z).split(' ')):
   print(ind, el[:10])

