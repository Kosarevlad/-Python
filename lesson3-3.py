#-----------------------первый вариант_________________

def my_func(num_1, num_2, num_3 ):
    my_list = [num_1, num_2, num_3]
    try:
        my_list.remove(min(my_list))
        return sum(my_list)
    except TypeError:
        return "Enter numbers only"

print(my_func(1, 2, 3))


#-----------------------второй вариант_________________

def personal_info(*args):
    return [*args]
x = personal_info(input("Первая цифра: "), input("Втораяая цифра: "), input("Третья цифра: "))
x.remove(min(x))

print(int(x[0]) + int(x[1]))
