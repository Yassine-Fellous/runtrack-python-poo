class Forme:
    def __init__(self):
        pass

    def aire(self):
        return 0


class Rectangle(Forme):

    def __init__(self, largeur, hauteur):
        super().__init__()
        self.__hauteur = hauteur
        self.__largeur = largeur

    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

    def aire(self):
        return self.__hauteur * self.__largeur


class Cercle(Forme):

    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def aire(self):
        return 3.14 * self.__radius ** 2


Rectangle1 = Rectangle(3, 4)
print(Rectangle1.get_largeur(), Rectangle1.get_hauteur(), Rectangle1.aire())

Cercle1 = Cercle(3)
print(Cercle1.get_radius(), Cercle1.aire())


