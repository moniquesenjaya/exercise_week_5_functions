def num_atoms(grams, atomic_weight = 196.97):
    avogadro = 6.02214076*pow(10,23)
    atoms = grams/atomic_weight*avogadro
    return atoms

print(num_atoms(10))
print(num_atoms(10, 12.001))
print(num_atoms(10, 1.008))