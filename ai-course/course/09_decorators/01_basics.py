from functools import wraps

def my_deco(fnc):
    @wraps(fnc)
    def wrapper():
        print("Befor function runs");
        fnc();
        print("Befor function runs");
    return wrapper;


@my_deco
def greet():
    print("Hello from deco class function")

greet()

print(greet.__name__)