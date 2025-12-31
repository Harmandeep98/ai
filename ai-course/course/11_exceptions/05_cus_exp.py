class OutOfIngs(Exception):
    pass

def makeTea(milk, sugar):
    if milk == 0 or sugar == 0:
        raise OutOfIngs("Missing Ings")
    print("Making chai")

makeTea(0, 1)