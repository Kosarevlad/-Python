def div(s_1, s_2):
    try:
        s_1, s_2 = int(s_1), int(s_2)
        div_num = s_1 / s_2
    except ValueError:
        return "ValueError"
    except ZeroDivisionError:
        return "Zoro"
    return round(div_num, 4)

print(div(input("Enter first num - "), input("Enter second num - ")))


