def telefon_bill():
    minutes = int(input("Количество минут: "))
    sms = int(input("Количество смс: "))
    mb = float(input("Количество МБ: "))
    
    base_minutes = 60
    base_sms = 30
    base_mb = 1024
    base_price = 24.99
    price_minutes = 0.89
    price_sms = 0.59
    price_mb = 0.79
    
    extra_minutes = 0
    if minutes > 60:
        extra_minutes = (minutes - 60) * 0.89
        
    extra_sms = 0
    if sms > 30:
        extra_sms = (sms - 30) * 0.59
        
    extra_mb = 0
    if mb > 1024:
        extra_mb = (mb - 1024) * 0.79
        
    total_no_tax = base_price + extra_minutes + extra_sms + extra_mb
    tax = total_no_tax * 0.02
    final_total = total_no_tax + tax

    print("Детализация счета ")
    print(f"Базовая сумма тарификации: {base_price:.2f} ")
    
    if extra_minutes > 0:
        print(f"Дополнительные минуты: {extra_minutes:.2f} ")
    if extra_sms > 0:
        print(f"Дополнительные SMS: {extra_sms:.2f} ")
    if extra_mb > 0:
        print(f"Дополнительный интернет: {extra_mb:.2f}")
        
    print(f"Налог: {tax:.2f} ")
    print(f"Итого: {final_total:.2f} ")


telefon_bill()