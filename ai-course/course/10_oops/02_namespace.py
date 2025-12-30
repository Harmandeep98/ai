# namespace in classes

class Chai:
    origin = "India"

print(Chai.origin)

Chai.isHot = True;

print(Chai.isHot)

# Creating objects from class chai

masala = Chai();

print(masala.origin)

Chai.isHot = False

print(Chai.isHot)
print(masala.isHot)
