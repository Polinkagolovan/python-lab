def compare_lists():
    text1=input("Первый набор чисел :")
    text2=input("Второй набор чиспол :")
    set1=set(text1.split())
    set2=set(text2.split())
    set3=set1&set2
    only_1=set1-set2
    only_2=set2-set1
    all_unique=set1^set2
    print("Все числа:",set3)
    print("Только в первом наборе:",only_1)
    print("Только во втором наборе:",only_2)
    print("Все кроме общих чисел:",all_unique)
compare_lists()