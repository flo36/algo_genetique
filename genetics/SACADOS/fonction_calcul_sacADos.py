from SACADOS.SacADos import SacADos

# on définit d'abord le problème :
# le poids de chaque objet :
tab_poids = [7, 8, 9, 3, 11, 5, 9, 7, 6, 2]

#le prix de chaque objet
tab_prix = [2, 18, 8, 5, 13, 8, 6, 10, 1, 5]
#le poids max que le sac peut contenir
poids_max = 25

#la valeur que l'on souhaite atteindre au minimum (pas forcément atteignable)
objectif_prix = 40

#création du problème
sac = SacADos(poids_max, tab_poids, tab_prix, objectif_prix)


def fonction_calcul_sacADos():

    return lambda chromosome: sac.note(chromosome)
