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


class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer.")

    def getMatiereEnseignee(self):
        return self.__matiereEnseignee

    def setMatiereEnseignee(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee

personne1 = Personne()
eleve1 = Eleve()

eleve1.affichageAge()