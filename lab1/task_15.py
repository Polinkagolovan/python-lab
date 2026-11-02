def list_analytics():
    list = [
        {"name": "Скрипка", "price": 60, "quantity": 6},
        {"name": "Гитара", "price": 80, "quantity": 5},
        {"name": "Фортепиано", "price": 90, "quantity": 19},
        {"name": "Гитара", "price": 50, "quantity": 7}
    ]

    revenues = {} 

    
    for item in list:
        name = item["name"]
        money = item["price"] * item["quantity"]
        
        if name in revenues:
            revenues[name] = revenues[name] + money
        else:
            revenues[name] = money

    print("\nВыручка по товарам:")
    for name in revenues:
        print(f"{name}: {revenues[name]} руб.")

    
    best_product = ""
    max_money = 0
    for name in revenues:
        if revenues[name] > max_money:
            max_money = revenues[name]
            best_product = name

    print(f"\nСамый прибыльный: {best_product} ({max_money} )")
    print(f"Всего уникальных наименований: {len(revenues)}")
list_analytics()
