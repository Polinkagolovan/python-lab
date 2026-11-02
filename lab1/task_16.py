def flatten_list(my_list):
    i = 0
    while i < len(my_list):
        if type(my_list[i]) == list:
            sub_list = my_list[i]
            del my_list[i]
            for item in reversed(sub_list):
                my_list.insert(i, item)
        else:
            i = i + 1

print("Программа начала работу...") 
list_a = [1, 2, 3, [4], 5, [6, [7, [], 8, [9]]]]
print("Исходный список:", list_a)

flatten_list(list_a)

print("Результат:", list_a)