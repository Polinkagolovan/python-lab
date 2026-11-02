def unique_elements(nested_list):
    result = set() 
    
    def extract(lst):
        for item in lst:
            if type(item) == list:
                extract(item) 
            else:
                result.add(item) 
                
    extract(nested_list)
    return list(result) 


list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
print("Исходный список:", list_a)
print("Уникальные элементы:", unique_elements(list_a))