FIO=input("Введите свою фамилию,имя,отчество:")
words = FIO.split()
if len(list)==3:
    print(f"В виде Фамилия И.О.:{list[0].capitalize()} {list[1][0].upper()}. {list[2][0].upper()}.")
else:
    print("Введите ФИО с пробелами")
