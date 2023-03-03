class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print("Age :", self.age)

    def bonjour(self):
        print("Hello")

    def modifierAge(self, age):
        self.age = age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def affichageAge(self):
        print("J'ai", self.age, "ans")


class Professeur(Personne):
    def __init__(self, age, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee
        super().__init__(age)

    def enseigner(self):
        print("Le cours va commencer.")

    def getMatiereEnseignee(self):
        return self.__matiereEnseignee

    def setMatiereEnseignee(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee


personne1 = Personne(15)
eleve1 = Eleve()

eleve1.bonjour()
eleve1.allerEnCours()

prof = Professeur(40, "Maths")
prof.bonjour()
prof.enseigner()
