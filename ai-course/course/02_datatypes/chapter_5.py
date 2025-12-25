# Strings

example_string = "Automatic String Slicing";

print(f"first word {example_string[0:9]}"); #last is not inclusive in python

print(f"first word {example_string[:9]}"); #easy pythonic code

print(f"after first word {example_string[9:]}"); #easy pythonic code

print(f"reversed words {example_string[::-1]}"); #reverse code in python

print(f"skip {example_string[0:9:2]}"); # every second character will be skipped

labled_text = example_string.encode("utf-8")