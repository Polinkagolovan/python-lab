cash=int(input("Введите сумму в рублях:"))
b100 = cash//100
remainder = cash %100
b50 = remainder//50
remainder = remainder %50
b10 = remainder//10
remainder = remainder%10
b5 = remainder//5
remainder = remainder%5
b2 = remainder//2
b1 = b2%1
print(f"Для размера суммы рублей потребуется:")
print(f"Купюр по 100 рублей :{b100}")
print(f"Купюр по 50 рублей :{b50}")
print(f"Купюр по 10 рублей :{b10}")
print(f"Купюр по 5 рублей :{b5}")
print(f"Купюр по 2 рублей :{b2}")
print(f"Купюр по 1 рублей :{b1}")

