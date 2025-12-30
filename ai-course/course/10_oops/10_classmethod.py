# class method in oops

class Chai_order:
    def __init__(self, type_, sweetness, size):
        self.type = type_;
        self.sweetness = sweetness;
        self.size = size;

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["type"],
            order_data["sweetness"],
            order_data["size"],
        )

    @classmethod
    def from_str(cls, order_data):
        type_, sweetness, size = order_data.split(",");
        return cls(type_, sweetness, size);

order1 = Chai_order.from_dict({"type": "Masala", "sweetness": "M", "size": "L"});

order2 = Chai_order.from_str("Ginger,M,L");

print(order1.__dict__)
print(order2.__dict__)
