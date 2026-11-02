age = int(input("Возраст заёмщика:"))
income  = float(input("Ежемесячный доход:"))
size= float(input("Размер запрашиваемого кредита : "))
month= int(input("Срок кредита(месяцы :)"))
history = input("Кредитная история(отличная/хорошая/удовлетворительная/плохая):")
ratio=size/income
print('Отношение кредита к доходу:', ratio)
risk=0
if ratio>10:
    risk=+3
elif ratio>5:
    risk=+2
if history=='плохая':
    risk=+3
elif history=='удовлетворительная ':
    risk=+1
if age < 21 or age > 65:
        risk = risk + 1
    
if risk >= 6:
        print("Риск: Критический. Рекомендация: Отклонить.")
elif risk >= 4:
        print("Риск: Высокий. Ставка: 18.5%")
elif risk >= 2:
        print("Риск: Средний. Ставка: 14%")
else:
        print("Риск: Низкий. Ставка: 10.5%")



