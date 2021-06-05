import numpy as np

# on définit d'abord le problème :
# le poids de chaque objet :
from SAT.Sat import Sat

#tableau des valeurs possibles pour les clauses
tab_predicat = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#ensemble de clauses à satisfaire, (l'instance du problème peut être solvable ou non)
tab_clause = [[-3],
              [3],
              [2, 0],
              [7, -3],
              [-1, -7],
              [6, 2],
              [8, -9],
              [5, -4]
              ]

#création du problème
sat = Sat(tab_clause, tab_predicat)


def fonction_calcul_sat():
    return lambda chromosome: sat.note(chromosome)
