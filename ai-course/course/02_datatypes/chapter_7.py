# Lists in python

ingrediants = ['water', 'milk', 'tea', 'sugar'];

ingrediants.append('cinnemon');
ingrediants.append('cardmom');
ingrediants.append('tea_masala');

print(f"Ingrediants are: {ingrediants}");

ingrediants.remove('tea_masala');

print(f"Ingrediants are: {ingrediants}");


array_example = [1, 2, 3, 4, 5];

array_example2 = [6, 7, 8, 9, 10];


final_array = array_example + array_example2;

print(f"Final array: {final_array}");

# Another example of array
array_example2.extend(array_example);
final_array2 = array_example2;

print(f"Final array 2: {final_array2}");

final_array3 = [*array_example2, *array_example];

print(f"Final array 3: {final_array3}");