class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque
        self.modele = modele
        self.annee = annee
        self.prix = prix

    def informationsVehicule(self):
        print("Marque : " + self.marque)
        print("Modele : " + self.modele)
        print("Année : " + str(self.annee))
        print("Prix : " + str(self.prix))

    def demarrer(self):
        print("Attention, je roule")


class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.porte = 4

    def informationsVehicule(self):
        print("Marque : " + self.marque)
        print("Modele : " + self.modele)
        print("Année : " + str(self.annee))
        print("Prix : " + str(self.prix))
        print("Porte : " + str(self.porte))

    def demarrer(self):
        print("Attention, je roule broom broom")

class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix):
        super().__init__(marque, modele, annee, prix)
        self.roue = 2

    def informationsVehicule(self):
        print("Marque : " + self.marque)
        print("Modele : " + self.modele)
        print("Année : " + str(self.annee))
        print("Prix : " + str(self.prix))
        print("roue : " + str(self.roue))

    def demarrer(self):
        print("Attention, je roule vroom vroom")


voiture1 = Voiture("Ferari", "ancien", 1985, 56000)
voiture1.informationsVehicule()
voiture1.demarrer()

moto1 = Moto("Honda", "mx125", 2020, 4400)
moto1.informationsVehicule()
moto1.demarrer()
