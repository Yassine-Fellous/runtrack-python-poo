class voiture:
    def __init__(self, marque, modèle, année, kilométrage):
        self.__marque = marque
        self.__modèle = modèle
        self.__année = année
        self.__kilométrage = kilométrage
        self.__en_marche = False
        self.__réservoir = 50

    def verifier_plein(self):
        return self.__réservoir

    def démarrer(self):
        if self.verifier_plein() >= 5 and not self.__en_marche:
            self.__en_marche = True
            return True
        else:
            return False

    def arreter(self):
        if self.__en_marche == True:
            self.__en_marche = False

    def get_marque(self):
        return self.__marque

    def set_marque(self, marque):
        self.__marque = marque

    def get_modèle(self):
        return self.__modèle

    def set_modèle(self, modèle):
        self.__modèle = modèle

    def get_année(self):
        return self.__année

    def set_année(self, année):
        self.__année = année

    def get_kilométrage(self):
        return self.__kilométrage

    def set_kilométrage(self, kilométrage):
        if kilométrage > 0:
            self.__kilométrage = kilométrage
        else:
            print("les kilométrage négatif n'existe pas")

    def set_réservoir(self, réservoir):
        if réservoir > 0:
            self.__réservoir = réservoir
        else:
            print("ce n'est pas possible d'avoir un réservoir négatif")

    def get_en_marche(self):
        return self.__en_marche

    def Info(self):
        print("marque =", self.__marque, "\n",
              "modèle =", self.__modèle, "\n",
              "année =", self.__année, "\n",
              "kilometrage =", self.__kilométrage, "\n",
              "en marche =", self.__en_marche, "\n",
              "réservoir =", self.__réservoir)


voiture1 = voiture("ferrari", "SF90 Stradale", 2023, 0)
voiture1.démarrer()
voiture1.arreter()
print(voiture1.get_en_marche())
