# list comprehension brief explanation

numbers = [1, 2, 3, 4, 5];

squared_numbers = [x**2 for x in numbers];

squared_numbers2 = [x**2 for x in numbers if x % 2 == 0];


print(f"Squared numbers: {squared_numbers}");
print(f"Squared numbers 2: {squared_numbers2}");