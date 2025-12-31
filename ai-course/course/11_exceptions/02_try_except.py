chai_menu = {"masala": 30, "ginger": 35}

try:
    chai_menu["eliachi"]
except KeyError:
    print("Unable to find the key")


print("Hi from the file")