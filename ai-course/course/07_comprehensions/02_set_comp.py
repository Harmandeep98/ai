# set comprehension brief explanation

spices = {'cardmom', 'cloves', 'cinnamon', 'cardmom', 'cinnamon', 'nutmeg'};

spices2 = {x + " spice" for x in spices};

print(f"Spices: {spices2}");


set = {
    "spcice": ["cardmom", "cloves", "cinnamon", "nutmeg"],
    "spice2": ["cardmom", "cloves", "cinnamon", "nutmeg", "masla spice", "black spice"]
};

unique_spice = {spice for types in set.values() for spice in types};

print(f"Set: {set.values()}");
print(f"Unique spice: {unique_spice}");