import random
number=random.randint(1,100)
while True :
    user_guess=int(input("Ваше число:"))
    if user_guess<number :
        print("Число больше")
    elif user_guess>number :
        print("Число меньше")
    else:
        print("Угадали число")
        break