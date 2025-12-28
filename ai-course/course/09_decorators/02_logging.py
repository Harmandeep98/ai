#logged with decorator

from functools import wraps;

def logger_deco(fnc):
    @wraps(fnc)
    def wrapper(*args, **kwargs):
        print(f"calling {fnc.__name__}")
        result = fnc(*args, **kwargs);
        print(f"finished {fnc.__name__}")
        return result;
    return wrapper;

@logger_deco
def brew_chai(type, milk="no"):
    print(f"Brewing {type} chai and milk status = {milk}");


brew_chai("masala chai");