my_list = list(input("введите цифры:"))
for el in range(1, len(my_list), 2):
    my_list[el-1], my_list[el] = my_list[el], my_list[el-1]
print(my_list)
