def numbers_analysis():
    text = input("Введите числа через пробел: ")
    parts = text.split()
    
    numbers = [] 
    for p in parts:
        if "." in p:
            numbers.append(float(p))
        else:
            numbers.append(int(p))
            
    
    unique = []
    duplicates = []
    for num in numbers:
        if num not in unique:
            unique.append(num) 
        else:
            if num not in duplicates:
                duplicates.append(num) 
                
    
    evens = []
    odds = []
    negatives = []
    floats = []
    for num in numbers:
        if num % 2 == 0:
            evens.append(num)
        else:
            odds.append(num)
            
        if num < 0:
            negatives.append(num)
            
        if isinstance(num, float): 
            floats.append(num)
            
    
    sum_5 = 0
    largest = numbers[0]
    smallest = numbers[0]
    for num in numbers:
        if num % 5 == 0:
            sum_5 = sum_5 + num
            
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
            
    print("Уникальные:", unique)
    print("Повторяющиеся:", duplicates)
    print("Четные:", evens)
    print("Нечетные:", odds)
    print("Отрицательные:", negatives)
    print("Дробные:", floats)
    print("Сумма кратных 5:", sum_5)
    print("Максимум:", largest)
    print("Минимум:", smallest)
numbers_analysis()

