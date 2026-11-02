
try:
    
    total_amount = float(input("Введите сумму покупки : "))
    age = int(input("Введите возраст покупателя: "))
    
    is_birthday = input("Сегодня день рождения покупателя? (да/нет): ").lower() == "да"
    is_vip = input("Покупатель является VIP-клиентом? (да/нет): ").lower() == "да"
    normal_discount = 0
    discount=0
    if total_amount>1000:
        normal_discount+=10
    if age>=63:
        normal_discount+=5
    if is_birthday:
        normal_discount+=5
    discount+=normal_discount
    if is_vip:
        if normal_discount>15:
            discount=normal_discount
        else:
            discount=15
    if discount>25:
        discount=25
    print(f"Ваша итоговая скидка:{discount}%\n Итоговая сумма:{total_amount-total_amount*discount/100}")
except ValueError:
    print("Ошибка: пожалуйста, вводите сумму и возраст только цифрами.")
