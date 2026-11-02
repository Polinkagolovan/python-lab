a=int(input("Введите первое число:"))
b=int(input("Введите второе число:"))
print("Сумма:" , a+b)
print("Разность: " , a-b)
print("Произведение:" , a*b)
print("Возведение в степень :", a**b)
print("Остаток от деления:", a%b)
try:
    print("Частное " , a/b)
except ZeroDivisionError :
    print("Деление на ноль запрещено")   
    
