class Livre:
    def __init__(self, titre, auteur, pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__pages = pages
        self.__disponibles = True

    def get_titre(self):
        return self.__titre

    def get_auteur(self):
        return self.__auteur

    def get_pages(self):
        return self.__pages

    def Emprunter(self):
            self.__disponibles = False

    def verification(self):
        if self.__disponibles == True:
            return True
        else:
            return False

    def rendre(self):
        if self.verification() == False:
            self.__disponibles = True

    def set_pages(self, pages):
        if pages > 0:
            self.__pages = pages
        else:
            print("pas de valeur négatif")

    def set_auteur(self, auteur):
            self.__auteur = auteur

    def set_titre(self, titre):
            self.__titre = titre


Livre1 = Livre("python", "moi", 48)
print(Livre1.get_titre(), Livre1.get_auteur(), Livre1.get_pages())
Livre1.set_auteur("pasmoi")
Livre1.set_pages(24)
Livre1.set_titre("ouifi")
print(Livre1.get_titre(), Livre1.get_auteur(), Livre1.get_pages(), Livre1.verification())
Livre1.Emprunter()
print(Livre1.get_titre(), Livre1.get_auteur(), Livre1.get_pages(), Livre1.verification())
Livre1.rendre()
print(Livre1.get_titre(), Livre1.get_auteur(), Livre1.get_pages(), Livre1.verification())