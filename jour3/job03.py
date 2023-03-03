class Tache:
    def __init__(self, titre, description):
        self.titre = titre
        self.description = description
        self.statut = "à faire"

    def __str__(self):
        return f"{self.titre} - {self.description} ({self.statut})"


class ListeDeTaches:

    def __init__(self):
        self.taches = []

    def ajouter_tache(self, tache):
        self.taches.append(tache)

    def supprimer_tache(self, tache):
        self.taches.remove(tache)

    def afficher_taches(self):
        if not self.taches:
            print("Aucune tâche à afficher")
        else:
            for tache in self.taches:
                print(tache)

