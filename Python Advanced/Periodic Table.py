n = int(input())
chemical_compounds = []

for _ in range(n):
    data = input().split()
    for el in data:
        chemical_compounds.append(el)

unique_chemical_compounds = set(chemical_compounds)

for el in unique_chemical_compounds:
    print(el)