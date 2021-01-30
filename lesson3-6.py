def sum_all():
    for word in input("Введите слова через пробел (латинские маленькие буквы)\n").split():
        x = 0
        for y in word:
            if 97 <= ord(y) <= 122:
                x += 1
        print(word.title() if x == len(word) else f"{word} - Только маленькие английские буквы")
sum_all()




