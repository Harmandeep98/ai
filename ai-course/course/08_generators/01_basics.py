def coffee_generator():
    yield "Espresso";
    yield "Latte";
    yield "Cappuccino";
    yield "Americano";
    yield "Flat White";
    yield "Macchiato";
    yield "Mocha";
    yield "Caramel Macchiato";
    yield "Iced Coffee";
    yield "Cold Brew";
    yield "Cold Brew Latte";
    yield "Cold Brew Macchiato";
    yield "Cold Brew Mocha";

for coffee in coffee_generator():
    print(f"Coffee: {coffee}");

coffee_generator_object = coffee_generator();

print(f"Coffee generator object: {coffee_generator_object}");

print(f"Coffee generator object next: {next(coffee_generator_object)}");

print(f"Coffee generator object next: {next(coffee_generator_object)}");

print(f"Coffee generator object next: {next(coffee_generator_object)}");


print(f"Coffee generator object next: {next(coffee_generator_object)}");