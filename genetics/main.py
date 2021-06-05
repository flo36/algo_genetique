from geneal.genetic_algorithms import BinaryGenAlgSolver

from SACADOS.fonction_calcul_sacADos import fonction_calcul_sacADos
from SAT.fonction_calcul_sat import fonction_calcul_sat



solver = BinaryGenAlgSolver(
    n_genes=10,
    fitness_function=fonction_calcul_sacADos(), #fonction_calcul_sat()
    n_bits=1,
    max_gen=50,
    pop_size=50,
    mutation_rate=0.05,
    selection_rate=0.3,
    selection_strategy="roulette_wheel"
)

solver.solve()