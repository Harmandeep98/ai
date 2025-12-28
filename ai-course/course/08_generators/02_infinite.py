
def infinite_generator():
    count = 1;

    while True:
        yield f"Coffee {count}";
        count += 1;

refill = infinite_generator();

for _ in range(10000):
    print(f"Refill: {next(refill)}");

print("All done :)")