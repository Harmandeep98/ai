# property decorators in python oops

class Tea_Leaf:
    def __init__(self, age):
        self._age = age;

    @property
    def age(self):
        return self._age + 2;

    @age.setter
    def age(self, age):
        if 1 <= age <= 5:
            self._age = age
        else:
            raise ValueError("Age must be b/w 1 and 5 years")

leaf = Tea_Leaf(3)

print(leaf.age)