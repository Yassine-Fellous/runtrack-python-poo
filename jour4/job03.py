class Rectangle:

    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur


class Parallélépipède(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur)
        super().__init__(largeur)
        self.__hauteur = hauteur

    def volume(self):
        volume = self.__longueur * self.__largeur * self.__hauteur
        return volume


rectangle1 = Rectangle(10, 5)
print("Longueur :", rectangle1.get_longueur())
print("Largeur :", rectangle1.get_largeur())
print("Périmètre :", rectangle1.perimetre())
print("Surface :", rectangle1.surface())
