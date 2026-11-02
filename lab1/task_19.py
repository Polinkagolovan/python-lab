def cache(func):
    memory = {} 
    
    def wrapper(*args):
        if args not in memory:
            print("Считаю в первый раз")
            memory[args] = func(*args) 
        else:
            print("Беру из памяти ")
            
        return memory[args]
    return wrapper

@cache
def square(x):
    return x * x

print("Первый вызов:", square(10))
print("Второй вызов:", square(10))