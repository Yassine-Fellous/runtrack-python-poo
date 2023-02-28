class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def Seprésenter(self):
        print("je suis", self.nom, self.prenom)


Personne1 = Personne("joe", "dalton")
Personne1.Seprésenter()

Personne1 = Personne("wi", "fi")
Personne1.Seprésenter()
