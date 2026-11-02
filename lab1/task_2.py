password = input("введите пароль:")
IsGood = True
if len(password)<16 :
    print("Пароль слишком короткий")
    IsGood =False
    if password.isdigit() or password.isalpha():
        print("Пароль слишком слабый ")
        IsGood = False
    if IsGood:
        print("Пароль надёжный")
    
    
