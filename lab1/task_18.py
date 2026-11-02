import datetime

def log_calls(filename):
    def decorator(func):
        def wrapper(*args):
            now = datetime.datetime.now()
            f = open(filename, "a", encoding="utf-8")
            f.write(f"Время: {now} | Функция: {func.__name__} | Аргументы: {args}\n")
            f.close()
            return func(*args)
        return wrapper
    return decorator

@log_calls("my_log.txt") 
def calculate_sum(a, b):
    return a + b
print("Результат задачи 18:", calculate_sum(5, 7))