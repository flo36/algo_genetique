
class Sat:
    """
    @:param _clauses : tableau de clause où une clause représente les prédicats voulus ou non par cette clause
    @:param _predicats : tableau contenant l'ensemble des prédicats
    """
    def __init__(self, _clauses, _predicats):
        self.clauses = _clauses
        self.nb_clause = len(_clauses)
        self.predicats = _predicats
        self.nb_predicat = len(_predicats)
        self.probleme_verifie = True
        self.nb_clause_verifiees = 0

    #méthode permettant de vérifier si la solution du problème satisfait son instance
    def verif_probleme(self, chromosome):
        num_clause = 0
        for clause in self.clauses:
            clause_verifie = False
            len_clause = len(clause)
            i = 0
            while i < len_clause and clause_verifie == False:
                predicat = clause[i]
                #clause respectée si le prédicat est positif et que le bit du chromosome est à 1
                if chromosome[abs(predicat)] == 1 and predicat == abs(predicat):
                    clause_verifie = True
                # clause respectée si le prédicat est négatif et que le bit du chromosome est à 0
                elif chromosome[abs(predicat)] == 0 and predicat != abs(predicat):
                    clause_verifie = True
                i += 1
            if clause_verifie == False:
                self.probleme_verifie = False
            else :
                self.nb_clause_verifiees += 1

    #méthode permettant d'attribuer une note à la solution proposée :
    #la note la plus haute est 0
    #Plus on s'approche de 0, plus le pourcentage de clause satisfaite est élevée
    def note(self, chromosome):
        self.nb_clause_verifiees = 0
        self.verif_probleme(chromosome)
        if self.probleme_verifie == True:
            #toutes les clauses sont vérifiées on attribue la note 0
            return 0
        else:
            #on attribue une note plus proche de 0 lorsqu'il y a plus de clauses vérifiées
            return self.nb_clause_verifiees/self.nb_clause*100 - 100