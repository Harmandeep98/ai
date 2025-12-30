class Chaicup:
    size = 150

    def descibe(self):
        return f"A cup is of {self.size}ml."

cup = Chaicup()
print(cup.descibe())
print(Chaicup.descibe(cup))