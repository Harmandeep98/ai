# sending value to the generator

def chai_customer():
    print("what chai would you like to have? :)");
    order = yield;

    while True:
        print(f"Preparing a {order} tea for you");
        order = yield;

tea_stall = chai_customer();

next(tea_stall) # start the generator

tea_stall.send("Macha");

tea_stall.send("Lemon");