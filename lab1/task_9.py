def converter():
    print("Типы: длина, масса, температура")
    measure_type = input("Введите тип измерения: ").lower()

    if measure_type == "длина":
        units = {"мм": 0.001, "см": 0.01, "м": 1.0, "км": 1000.0}
        print("Доступные единицы:", list(units.keys()))
        from_unit = input("Из какой единицы: ").lower()
        to_unit = input("В какую единицу: ").lower()
        value = float(input("Значение: "))
        
        if from_unit in units and to_unit in units:
            res = value * (units[from_unit] / units[to_unit])
            print(f"{value} {from_unit} = {res} {to_unit}")
        else:
            print("Ошибка: неверные единицы")

    elif measure_type == "масса":
        units = {"мг": 0.001, "г": 1.0, "кг": 1000.0, "т": 1000000.0}
        print("Доступные единицы:", list(units.keys()))
        from_unit = input("Из какой единицы: ").lower()
        to_unit = input("В какую единицу: ").lower()
        value = float(input("Значение: "))
        
        if from_unit in units and to_unit in units:
            res = value * (units[from_unit] / units[to_unit])
            print(f"{value} {from_unit} = {res} {to_unit}")
        else:
            print("Ошибка: неверные единицы")

    elif measure_type == "температура":
        from_unit = input("Из какой (C, F, K): ").upper()
        to_unit = input("В какую (C, F, K): ").upper()
        value = float(input("Значение: "))
        
        if from_unit == "C":
            c = value
        elif from_unit == "F":
            c = (value - 32) * 5 / 9
        elif from_unit == "K":
            c = value - 273.15
        else:
            print("Ошибка ввода"); return

        if to_unit == "C":
            res = c
        elif to_unit == "F":
            res = c * 9 / 5 + 32
        elif to_unit == "K":
            res = c + 273.15
        else:
            print("Ошибка ввода"); return

        print(f"{value} {from_unit} = {res} {to_unit}")
    else:
        print("Неизвестный тип измерения")
converter()