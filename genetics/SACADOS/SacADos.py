
class SacADos:
    """
    @:param _poids : poids maximum que le sac peut contenir
    @:param _objetsPoids : tableau avec le poid de chaque objet
    @:param _objetsPrix : tableau avec le prix de chaque objet
    @:param _objectif_prix : objectif de prix à atteindre, peut être ou non atteignable
    """
    def __init__(self, _poids, _objetsPoids, _objetsPrix, _objectif_prix):
        self.poids = _poids
        self.objets = _objetsPoids
        self.nb_objet = len(_objetsPoids)
        self.prix = _objetsPrix
        self.objectif_prix = _objectif_prix

    """
    @:param objets_coisis : tableau de bit où 1 représente la présence de l'objet dans le sac et 0 non
    @:return boolean : vrai si le poids max n'est pas 
    """
    def poids_bon(self, objets_choisis):
        poids_cumule = 0
        for i in range(len(objets_choisis)-1):
            if objets_choisis[i] == 1:
                print(i)
                #le bit pour cet objet est à 1, on compte le poids de l'objet
                poids_cumule += self.objets[i]
        if poids_cumule > self.poids:
            return False
        else:
            return True

    """
    @:param objets_coisis : tableau de bit où 1 représente la présence de l'objet dans le sac et 0 non
    @:return prix_cumule : le prix que représente l'ensemble des objets choisis 
    """
    def prix_final(self, objets_choisis):
        prix_cumule = 0
        for i in range(len(objets_choisis)-1):
            if objets_choisis[i] == 1:
                #le bit pour cet objet est à 1, on compte le poids de l'objet
                prix_cumule += self.prix[i]

        return prix_cumule

    def note(self, objets_choisis):
        poids_correct = self.poids_bon(objets_choisis)
        note = 0
        prix_calcule = self.prix_final(objets_choisis)
        if poids_correct:
            note = prix_calcule/self.objectif_prix*100 - 100
        else:
            note = -100

        return note



