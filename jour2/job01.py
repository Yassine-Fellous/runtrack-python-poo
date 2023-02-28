class  rectangle:
    def __init__(self, longeur, largeur):
        self.__longeur = longeur
        self.__largeur = largeur

    def get_largeur(self):
        return self.__largeur

    def get_longeur(self):
        return self.__longeur

    def set_largeur(self, largeur):
            self.__largeur = largeur

    def set_longeur(self, longeur):
            self.__longeur = longeur


rectangle1 = rectangle(3, 4)
print(rectangle1.get_largeur(), rectangle1.get_longeur())
rectangle1.set_largeur(6)
rectangle1.set_longeur(4)
print(rectangle1.get_largeur(), rectangle1.get_longeur())