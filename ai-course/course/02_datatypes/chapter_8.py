#sets
essenial_spices = {"cardmom", "ginger", "cloves", "turmeric"};

print(f"Essential spices: {essenial_spices}");

essenial_spices2 = {"cardmom", "ginger", "cloves", "cardmom", "cinnamon", "nutmeg"};

print(f"Essential spices2: {essenial_spices2}");

essenial_spices3 = essenial_spices.union(essenial_spices2);

essenial_spices3 = essenial_spices.intersection(essenial_spices2);