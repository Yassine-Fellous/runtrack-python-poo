class Produit:

    def __init__(self, nom, prix, TVA):
        self.nom = nom
        self.prix = prix
        self.TVA = TVA
        self.prix_ttc = 0

    def changer_nom(self, nom):
        self.nom = nom

    def changer_prix(self, prix):
        self.prix = prix

    def afficher_prix_HT(self):
        return self.prix

    def afficher_nom(self):
        return self.nom

    def afficher_tva(self):
        return self.TVA

    def Calculer_Prix_TTC(self):
        montant_tva = self.prix * self.TVA / 100
        prix_ttc = self.prix + montant_tva
        self.prix_ttc = prix_ttc
        return prix_ttc


produit1 = Produit("box4g", 100, 20)
print("Nom_produit :", produit1.afficher_nom(), "Prix HT :", produit1.afficher_prix_HT(), "Taux de TVA :", produit1.afficher_tva(), "Prix TTC :", produit1.Calculer_Prix_TTC())
produit1.changer_prix(120)
produit1.changer_nom("box5g")
print("Nom_produit :", produit1.afficher_nom(), "Prix HT :", produit1.afficher_prix_HT(), "Taux de TVA :", produit1.afficher_tva(), "Prix TTC :", produit1.Calculer_Prix_TTC())

produit2 = Produit("iphone14", 10016, 15)
print("Nom_produit :", produit2.afficher_nom(), "Prix HT :", produit2.afficher_prix_HT(), "Taux de TVA :", produit2.afficher_tva(), "Prix TTC :", produit2.Calculer_Prix_TTC())
produit2.changer_prix(1446)
produit2.changer_nom("iphone15")
print("Nom_produit :", produit2.afficher_nom(), "Prix HT :", produit2.afficher_prix_HT(), "Taux de TVA :", produit2.afficher_tva(), "Prix TTC :", produit2.Calculer_Prix_TTC())