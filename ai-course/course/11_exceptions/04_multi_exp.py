# multiple exception in python

def process_order(item, qty):
    try:
        price = {"masala":20,"ginger":10}[item];
        cost = price * qty;
        print(f"Total cost is {cost}")
    except KeyError:
        print("Sorry this item is not on menu")
    except TypeError:
        print("Please enter the number of items")