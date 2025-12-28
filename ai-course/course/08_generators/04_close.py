# yield from and close in generators

def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"


def imported_chai():
    yield "Macha"
    yield "Oolong"


def full_menu():
    yield from local_chai();
    yield from imported_chai();


for chai in full_menu():
    print(chai);


def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order";
    except:
        print("Stall closed no more chai");

stall = chai_stall();

print(next(stall));

stall.close()