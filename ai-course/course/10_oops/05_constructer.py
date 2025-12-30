class ChaiOrder:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size}ml of {self.type}";


newOrder = ChaiOrder("Masala", 100);

print(newOrder.summary());