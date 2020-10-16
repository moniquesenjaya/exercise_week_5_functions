def num_atoms(grams, atomic_weight = 196.97):
    avogadro = 6.02214076*pow(10,23)
    atoms = grams/atomic_weight*avogadro
    print(atoms)

num_atoms(10)
num_atoms(10, 12.001)
num_atoms(10, 1.008)