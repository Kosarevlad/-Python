def sum_all():
    s = 0
    while True:
        in_list = input("Введите значения. Для остановки программы введите 'q'").split()
        for num in in_list:
            if num == 'q':
                return s
            else:
                try:

                    s += int(num)
                except ValueError:
                    print("Для выхода Enter 'q")
        print(f"сумма значений - {s}")

print(sum_all())


