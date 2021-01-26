my_list = [15, 1.5, 'qwerty', False, [1, 2], (5+6j), (1, 2, 6), {1, 4, 5}, {26: 11, 3: 2}]
new_list =[]
x = 0
for el in my_list:

    new_list.append(type(el))
x = 0

for ind, el in enumerate(new_list):
    print(ind, my_list[x], '''Это''', el)
    x = x + 1

