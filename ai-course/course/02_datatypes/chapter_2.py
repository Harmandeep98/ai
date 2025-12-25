spice_mix = set();
print(f"Initial spice mix id: {id(spice_mix)}");
spice_mix.add("Ginger");
spice_mix.add("cardamom");
print(f"After spcie mix id: {id(spice_mix)}");

spice_mix = [];

print(f"ID after changing datatype id: {id(spice_mix)}")