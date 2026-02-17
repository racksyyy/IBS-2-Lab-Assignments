from itertools import product

amino_acid_masses = [
    57, 71, 87, 97, 99, 101, 103,
    113, 114, 115, 128, 129, 131,
    137, 147, 156, 163, 186
]

def cyclic_spectrum(peptide):
    prefix_mass = [0]
    for mass in peptide:
        prefix_mass.append(prefix_mass[-1] + mass)
    peptide_mass = prefix_mass[-1]
    spectrum = [0]
    n = len(peptide)
    for i in range(n):
        for j in range(i + 1, n + 1):
            spectrum.append(prefix_mass[j] - prefix_mass[i])
            if i > 0 and j < n:
                spectrum.append(peptide_mass - (prefix_mass[j] - prefix_mass[i]))
    return sorted(spectrum)


def brute_force_cyclopeptide_sequencing(parent_mass, experimental_spectrum):
    results = []
    peptides = [[]]
    while peptides:
        new_peptides = []
        for peptide in peptides:
            for mass in amino_acid_masses:
                new_peptide = peptide + [mass]
                total_mass = sum(new_peptide)
                if total_mass == parent_mass:
                    if cyclic_spectrum(new_peptide) == sorted(experimental_spectrum):
                        results.append(new_peptide)
                if total_mass <= parent_mass:
                    new_peptides.append(new_peptide)
        peptides = new_peptides
    return results

experimental_spectrum = [0, 113, 128, 186, 241, 299, 314, 427] 
parent_mass=experimental_spectrum[-1]
solutions = brute_force_cyclopeptide_sequencing(parent_mass, experimental_spectrum)

print("Matching Peptides:")
for i in solutions:
    print(i)
