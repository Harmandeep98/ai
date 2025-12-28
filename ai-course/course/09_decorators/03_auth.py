#logged with decorator

from functools import wraps;

def require_admin(fnc):
    @wraps(fnc)
    def wrapper(user_roles):
        if user_roles != "admin":
            print("You are not allowed");
            return None
        else:
            return fnc(user_roles);
    return wrapper;


@require_admin
def access_tea_inv(role):
    print("Access granted to inv")


access_tea_inv("user")

access_tea_inv("admin")