class Ville:
    def __init__(self, nom, nb_habitants):
        self.__nom = nom
        self.__nb_habitants = nb_habitants

    def get_nb_habitants(self):
        return self.__nb_habitants

    def set_nb_habitants(self, new_nb_number):
        self.__nb_habitants = new_nb_number


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville
        self.ajouterPopulation()

    def ajouterPopulation(self):
        new_nb_habitants = self.__ville.get_nb_habitants() + 1
        self.__ville.set_nb_habitants(new_nb_habitants)



paris = Ville("Paris", 1000000)
print(paris.get_nb_habitants())

marseille = Ville("Marseille", 861635)
print(marseille.get_nb_habitants())

john = Personne("John", 45, paris)
myrtille = Personne("Myrtille", 4, paris)
chloe = Personne("Chloé", 18, marseille)

print(paris.get_nb_habitants())
print(marseille.get_nb_habitants())